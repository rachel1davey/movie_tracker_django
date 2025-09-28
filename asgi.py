"""
ASGI config for movie_tracker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'movie_tracker'))


from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_tracker.settings')

application = get_asgi_application()
