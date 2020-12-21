"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z+ksf@)0d^qojbh4rnp4b1to$hq&*tt(3bs$gf(3i267g$k9ln'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['rozpanthiras.herokuapp.com','127.0.0.1','localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'store.apps.StoreConfig',

    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'webcommerce',
        'USER': 'postgres',
        'PASSWORD': 'vasi1993',
        'HOST': 'localhost'
    }
}
temp_db = dj_database_url.config()
if temp_db:
    DATABASES['default'] = temp_db


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# STATIC FILES (CSS, JavaScript, Images) 
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# STATIC_URL is the URL used when referring to static files. It must end with / if it is set to any value except None. 
# The following path means that static files will be stored in the location http://localhost:8000/static/ 
STATIC_URL = '/static/'
# STATIC_ROOT is the path that defines where your static files will be collected.
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
# To use a commonplace for all static files in your project directory, we need to configure STATICFILES_DIRS to inform Django 
# about our new directory because AppDirectoriesFinder will look for static in app directories only.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/images/'

####### MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#set S3 as the place to store your files.
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = "AKIARHYDLB3L4KIB73X5"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "vasilisskouteris18122020"
AWS_QUERYSTRING_AUTH = False #This will make sure that the file URL does not have unnecessary parameters like your access key.
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME + ".s3.amazonaws.com" 

AWS_DEFAULT_ACL ="public-read"
AWS_LOCATION = "static"

STATIC_URL = 'https://' + AWS_S3_CUSTOM_DOMAIN +"static/"
MEDIA_URL  = 'https://' + AWS_S3_CUSTOM_DOMAIN + "media/"
STATICFILES_DIRS = ( os.path.join(BASE_DIR, "static"), )
STATIC_ROOT = "staticfiles"
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"
STATICFILES_FINDERS = (
"django.contrib.staticfiles.finders.FileSystemFinder",
"django.contrib.staticfiles.finders.AppDirectoriesFinder",
)