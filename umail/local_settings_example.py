# -*- coding: utf8 -*-
EMAIL_USE_TLS = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

#Configuración de envío de correo por Gmail
EMAIL_USE_TLS = True # Control para cuando se use un sitio con conexión segura
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '' #CUENTA DE CORREO 
EMAIL_HOST_PASSWORD = '' #CONTRASEÑA DE CORREO


CACHES={
        'default':{
                'BACKEND':'django.core.cache.backends.filebased.FileBasedCache',
                'LOCATION':'/tmp/'
        }
}

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle.'
        'NAME': '',
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
