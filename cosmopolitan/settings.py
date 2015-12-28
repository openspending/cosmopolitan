"""
Django settings for cosmopolitan project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-2%$qx$=8gc4_zf36$ugzo%an8@==x-e9dr_plwtt*@2j4hovg'

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv('DEBUG', False):
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'rest_framework',
    'cities',
    'world',
    'continents',
    'currencies',
    'extra_countries'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'middleware.url.LowercaseMiddleware',
)

ROOT_URLCONF = 'cosmopolitan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cosmopolitan.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

if os.getenv('LOCAL_DEV', False):
    DATABASES = {
        'default': {
            'NAME': 'cosmopolitan',
            'USER': 'cosmopolitan',
            'PASSWORD': '123456',
        }
    }
elif os.getenv('BUILD_ON_TRAVIS', None):
    SECRET_KEY = "SecretKeyForUseOnTravis"
    TEMPLATE_DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'travis_ci_test',
            'USER': 'travis',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
        }
    }
else:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}
    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}
