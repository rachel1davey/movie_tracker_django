import os
import sys

# Add outer movie_tracker folder to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'movie_tracker'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_tracker.settings')

application = get_wsgi_application()
