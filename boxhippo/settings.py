"""
Django settings for boxhippo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l#1!a!$o4q%$*c#e$9ehr8^(5_p_#(ixpekx#6+x#o&zy2(!bj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


TEMPLATE_DEBUG = True

template_dir = "/var/www/boxhippo/templates"
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), template_dir).replace('\\', '/'),
)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.boxhippo.com']


# Application definition

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'listings',
    'users',
    'widget_tweaks',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'boxhippo.urls'

WSGI_APPLICATION = 'boxhippo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
		'read_default_file': '/var/www/boxhippo/db.cnf',
	},
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, "static"),
  "/var/www/boxhippo/static/",
)

MEDIA_ROOT = '/var/www/boxhippo/static/'
MEDIA_URL = '/media/'
"""
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
MEDIA_ROOT = '/var/www/boxhippo/boxhippo/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/var/www/boxhippo/boxhippo/static/'
STATIC_URL = '/static/'


STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
"""
