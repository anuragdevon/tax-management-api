"""
WSGI config for gms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

DJANGO_SERVICE_MODULE = os.environ.get('DJANGO_SERVICE_MODULE')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SERVICE_MODULE)

application = get_wsgi_application()
