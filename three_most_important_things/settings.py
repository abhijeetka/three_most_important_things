"""
Django settings for three_most_important_things project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
TEST_OUTPUT_VERBOSE = 2
TEST_OUTPUT_DESCRIPTIONS = True
TEST_OUTPUT_DIR = "./reports/"





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$%ap$ba8l+!mexp#(1bc1uyk7uojn*rgydi0wr73rir+5hul*c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jenkins',
    'polymer',
    'accounts',
)


#INSTALLED_APPS += ('django_jenkins',)
#JENKINS_TASKS = ()
JENKINS_TASKS = (
    
  #  'django_jenkins.tasks.run_csslint',
   # 'django_jenkins.tasks.run_scsslint',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    'django_jenkins.tasks.run_flake8',
  #  'django_jenkins.tasks.run_pylint'
  #  'django_jenkins.tasks.run_sloccount',
  #  'django_jenkins.tasks.with_coverage',
#    'django_jenkins.tasks.django_tests',
)

PROJECT_APPS = [appname for appname in INSTALLED_APPS if appname.startswith('three_most_important_things project')]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'three_most_important_things.urls'

WSGI_APPLICATION = 'three_most_important_things.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/static'
STATICFILES_DIRS = (
    BASE_DIR + '/assets',
)

try:
    from local_settings import *
except ImportError as exp:
    pass
