#!/usr/bin/env python3
import subprocess
import sys
import os

repo_root = os.path.dirname(os.path.abspath(__file__))

os.chdir(repo_root)

def run(cmd, capture=False):
    if capture:
        return subprocess.check_output(cmd, shell=True, text=True).strip()
    else:
        subprocess.check_call(cmd, shell=True)

# 1. Ensure clean working tree or stash
status = run('git status --porcelain', capture=True)
stashed = False
if status:
    print('Stashing local changes...')
    run("git stash push -u -m 'pre-rewrite-stash'")
    stashed = True

# 2. Resolve base commit (HEAD~12)
base = run('git rev-parse --verify HEAD~12', capture=True)
print('Base commit:', base)

# 3. Create temp branch at base
new_branch = 'rewrite-temp'
# ensure no existing branch
try:
    run(f'git branch -D {new_branch} || true')
except Exception:
    pass
run(f'git checkout -b {new_branch} {base}')

# 4. mapping
mapping = {
    '2ee296e': 'Show signup success toast via allauth signal',
    '42750a0': 'Show signup success toast via allauth signal',
    '301ef0b': 'Show toast on review/profile changes and on login/logout',
    '3032d99': 'Show toast on review/profile changes and on login/logout',
    '8349b77': 'Add accessible toast container + JS',
    '39ed384': 'Fix login template: preserve input and show errors',
    'eaa1fd8': 'Render login inputs and display field/non-field errors',
    '6068bd4': 'Show login errors, preserve login value; match index/results rating style',
    '30282ca': 'Show login errors, preserve login value; match index/results rating style',
    'cedf1e9': 'Match index poster size/layout with search results',
    '527e77a': 'Match index poster size/layout with search results',
    '4d8b4e1': 'Fix avatar tag load; style profile and review pages',
}

# 5. iterate commits
revlist = run('git rev-list --reverse HEAD~12..HEAD', capture=True).splitlines()
for h in revlist:
    print('Processing', h)
    # cherry-pick without commit
    run(f'git cherry-pick {h} -n')
    # get author and date
    author = run(f"git show -s --format='%an <%ae>' {h}", capture=True)
    date = run(f"git show -s --format='%aI' {h}", capture=True)
    newmsg = mapping.get(h)
    if not newmsg:
        newmsg = run(f"git log --format=%s -n 1 {h}", capture=True)
    # commit with original metadata
    env = os.environ.copy()
    env['GIT_COMMITTER_DATE'] = date
    subprocess.check_call(['git', 'commit', '--author', author, '--date', date, '-m', newmsg], env=env)

# 6. move main to new history
run('git checkout main')
run(f'git reset --hard {new_branch}')

# 7. push force-with-lease
print('Pushing rewritten history...')
run('git push --force-with-lease origin main')

# 8. cleanup
run(f'git branch -D {new_branch} || true')

if stashed:
    print('Popping stash...')
    try:
        run('git stash pop')
    except Exception as e:
        print('Failed to pop stash:', e)

print('Done. Recent commits:')
print(run('git --no-pager log --oneline -n 12', capture=True))
