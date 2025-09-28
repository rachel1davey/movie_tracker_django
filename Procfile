web: gunicorn movie_tracker.movie_tracker.wsgi
tailwind: python manage.py tailwind install && npm ci --prefix theme/static_src --include=dev && python manage.py tailwind build