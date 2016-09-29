import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ALLOWED_HOSTS = []

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myblog',
        'USER': 'slava',
        'PASSWORD': 'nytulqxe',
        'HOST': 'localhost',
        'PORT': '',
    }
}

SESSION_COOKIE_SECURE = False
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER  = False
SECURE_SSL_REDIRECT = False
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
