from django.db import migrations


class Migration(migrations.Migration):

    # Merge the two migration branches: the branch that altered profile.bio/avatar
    # and the branch that deleted MovieList.
    dependencies = [
        ("core", "0003_alter_profile_avatar"),
        ("core", "0002_delete_movielist"),
    ]

    operations = []
