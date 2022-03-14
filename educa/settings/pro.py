from distutils.debug import DEBUG
from .base import *

DEBUG = False

ADMINS = (
    ('admin', 'evgsles@yandex.ru'),
)

ALLOWED_HOSTS = ['.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '0000',
        'HOST': '127.0.0.1',
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True