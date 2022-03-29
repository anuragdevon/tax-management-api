from .base import *

ALLOWED_HOSTS = ["*"]

WSGI_APPLICATION = 'gms.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
