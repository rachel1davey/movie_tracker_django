"""
Django settings for movie_tracker project.
"""

from decouple import config
from pathlib import Path
import os
import environ
import dj_database_url

# ------------------------------
# Base directory
# ------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------
# Environment variables
# ------------------------------
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = config("SECRET_KEY", default="django-insecure-fallback-key")
DEBUG = config("DEBUG", cast=bool, default=False)

_default_allowed_hosts = "moviebucketdjango-03c8d5ee1edd.herokuapp.com,localhost,127.0.0.1,.herokuapp.com"
ALLOWED_HOSTS = [h.strip() for h in config("ALLOWED_HOSTS", default=_default_allowed_hosts).split(",") if h.strip()]

CSRF_TRUSTED_ORIGINS = [o.strip() for o in config("CSRF_TRUSTED_ORIGINS", default="https://*.herokuapp.com").split(",") if o.strip()]

# ------------------------------
# Installed Apps
# ------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'tailwind',
    'theme',
    'movie_tracker.core',
    'movie_tracker.movies',
]

if DEBUG:
    INSTALLED_APPS += ['django_browser_reload']

TAILWIND_APP_NAME = 'theme'

# ------------------------------
# Middleware
# ------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

if DEBUG:
    MIDDLEWARE += ["django_browser_reload.middleware.BrowserReloadMiddleware"]

# ------------------------------
# URLs and WSGI
# ------------------------------
ROOT_URLCONF = 'movie_tracker.movie_tracker.urls'
WSGI_APPLICATION = 'movie_tracker.movie_tracker.wsgi.application'

# ------------------------------
# Templates
# ------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ------------------------------
# Database
# ------------------------------
if "DATABASE_URL" in os.environ:
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ------------------------------
# Password validators
# ------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------
# Internationalization
# ------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------
# Static files
# ------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

# Ensure theme/static exists so Django W004 warning disappears
STATICFILES_DIRS = [
    BASE_DIR / "theme" / "static",  # <-- make sure this folder exists with empty .gitkeep if needed
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ------------------------------
# Default primary key field type
# ------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ------------------------------
# Site and authentication
# ------------------------------
SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_SIGNUP_FIELDS = ['email', 'username*', 'password1*', 'password2*']
LOGIN_REDIRECT_URL = "/profile/"

# ------------------------------
# API Keys
# ------------------------------
TMDB_API_KEY = config("TMDB_API_KEY", default="")

# ------------------------------
# Notes:
# - Make sure theme/static/theme/css/dist exists with Tailwind build
# - In production, build Tailwind in release phase:
#   npm ci --prefix theme/static_src --include=dev && npm run --prefix theme/static_src build
# - Then run: python manage.py collectstatic --noinput
# ------------------------------
