from decouple import config
from pathlib import Path
import os
import environ
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------
# Environment
# ----------------------
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = config("SECRET_KEY", default="django-insecure-fallback-key")
DEBUG = config("DEBUG", cast=bool, default=False)  # False in production

# Allowed hosts
_default_allowed_hosts = "localhost,127.0.0.1,moviebucketdjango-03c8d5ee1edd.herokuapp.com,.herokuapp.com"
ALLOWED_HOSTS = [
    h.strip()
    for h in config("ALLOWED_HOSTS", default=_default_allowed_hosts).split(",")
    if h.strip()
]

CSRF_TRUSTED_ORIGINS = [
    o.strip()
    for o in config(
        "CSRF_TRUSTED_ORIGINS",
        default="http://localhost,https://*.herokuapp.com"
    ).split(",")
    if o.strip()
]

# ----------------------
# Apps
# ----------------------
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
    'movie_tracker.chat'
]

# Only enable django-browser-reload locally
RUN_BROWSER_RELOAD = config("RUN_BROWSER_RELOAD", cast=bool, default=False)
if DEBUG and RUN_BROWSER_RELOAD:
    INSTALLED_APPS += ['django_browser_reload']

TAILWIND_APP_NAME = 'theme'

# ----------------------
# Middleware
# ----------------------
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

# Only include browser reload middleware locally
if DEBUG and RUN_BROWSER_RELOAD:
    MIDDLEWARE += ["django_browser_reload.middleware.BrowserReloadMiddleware"]

# ----------------------
# URLs and Templates
# ----------------------
ROOT_URLCONF = 'movie_tracker.movie_tracker.urls'
WSGI_APPLICATION = 'movie_tracker.movie_tracker.wsgi.application'

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

# ----------------------
# Database
# ----------------------
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

# ----------------------
# Auth
# ----------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1
ACCOUNT_SIGNUP_FIELDS = ['email', 'username*', 'password1*', 'password2*']
LOGIN_REDIRECT_URL = "/profile/"

# ----------------------
# Internationalization
# ----------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------------
# Static files
# ----------------------
STATICFILES_DIRS = [
    BASE_DIR / "theme" / "static",             # Tailwind compiled CSS
    BASE_DIR / "movie_tracker" / "static",     # fallback
]

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ----------------------
# Primary Key
# ----------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ----------------------
# API Keys
# ----------------------
TMDB_API_KEY = config("TMDB_API_KEY", default="")
