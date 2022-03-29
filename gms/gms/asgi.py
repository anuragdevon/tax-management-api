"""
ASGI config for gms project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

DJANGO_SERVICE_MODULE = os.environ.get('DJANGO_SERVICE_MODULE')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SERVICE_MODULE)

application = get_asgi_application()
