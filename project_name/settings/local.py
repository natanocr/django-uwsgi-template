"""Django settings for local environment."""

from {{project_name}}.settings.base import *  # noqa
from {{project_name}}.settings.secret import *  # noqa

HOST = '{{project_name}}.local'

ALLOWED_HOSTS = (HOST, '127.0.0.1', 'localhost')


# Database
# https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATABASES_DEFAULT_NAME or '{{project_name}}',  # noqa
        'USER': DATABASES_DEFAULT_USER or '{{project_name}}',  # noqa
        'PASSWORD': DATABASES_DEFAULT_PASSWORD or '',  # noqa
        'HOST': DATABASES_DEFAULT_HOST or '127.0.0.1',  # noqa
        'PORT': DATABASES_DEFAULT_PORT or '5432',  # noqa
    }
}


# Email Settings
# https://docs.djangoproject.com/en/{{docs_version}}/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

EMAIL_FILE_PATH = '/tmp/app-messages'


# Debug

DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa


# Debug Toolbar

try:
    import debug_toolbar  # noqa
except ModuleNotFoundError:
    pass
else:
    INTERNAL_IPS = ['127.0.0.1', 'localhost']
    INSTALLED_APPS.append('debug_toolbar')  # noqa
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')  # noqa
