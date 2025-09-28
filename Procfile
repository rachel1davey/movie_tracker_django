# Run Tailwind to compile CSS (Heroku will run this during build)
release: python manage.py tailwind install && python manage.py tailwind build

# Run the web server
web: gunicorn movie_tracker.movie_tracker.wsgi --log-file -