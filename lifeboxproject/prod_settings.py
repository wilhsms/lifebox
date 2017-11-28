from .settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lifebox$default',
        'USER': 'lifebox',
        'PASSWORD': 'vermelho@123',
        'HOST': 'lifebox.mysql.pythonanywhere-services.com',
    }
}

# REST_FRAMEWORK CONFIG
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'COERCE_DECIMAL_TO_STRING': False
}