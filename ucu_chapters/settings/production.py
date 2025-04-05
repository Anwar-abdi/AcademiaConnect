from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = ['*.onrender.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ucu_chapters_db',
        'USER': 'root',
        'PASSWORD': 'Anwar2017',
        'HOST': 'localhost',
        'PORT': '3306',  # Switch back to working port
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

# Required for Render deployment
STATIC_URL = '/static/'
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'