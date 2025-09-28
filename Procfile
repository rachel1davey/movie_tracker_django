web: gunicorn movie_tracker.movie_tracker.wsgi
tailwind: npm ci --prefix theme/static_src --include=dev && npm run --prefix theme/static_src build
release: npm ci --prefix theme/static_src --include=dev && npm run --prefix theme/static_src build && python manage.py migrate --noinput && python manage.py collectstatic --noinput