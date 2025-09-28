# Build Tailwind CSS on deploy
release: python manage.py tailwind install && python manage.py tailwind build

# Start the web server
web: gunicorn movie_tracker.wsgi --log-file -