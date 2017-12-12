# -*- coding: utf-8 -*-
from .settings import *

DEBUG = True

ALLOWED_HOSTS = [u'lifebox.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lifebox$default',
        'USER': 'lifebox',
        'PASSWORD': 'vermelho@123',
        'HOST': 'lifebox.mysql.pythonanywhere-services.com',
    }
}

#Descomentar assim que a autenticação for adicionada no equipamento
'''
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
'''
'''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'MYAPP': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}
'''