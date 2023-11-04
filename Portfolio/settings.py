"""
Django settings for Portfolio project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
import boto3
from decouple import config
from storages.backends.s3boto3 import S3Boto3Storage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  "h-1&^(+t9&c40b2*dxo@m^zux@xuzfhay^zvh%mnw3is^)r288"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'portapp',
    'jazzmin',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Decouple app
    'decouple',
    'storages',
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'portapp', 'templates', 'portapp'),],
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

WSGI_APPLICATION = 'Portfolio.wsgi.application'


JAZZMIN_SETTINGS = { 
    "site_title": "SG Dashboard",
    "site_header": "SG",
    "site_logo": 'vendor/adminlte/img/AdminLTELogo.jpg',
    "login_logo": None,
    "welcome_sign": "Welcome to the SG Dashboard",
    # Copyright on the footer
    "copyright": "SG",
    
    'site_brand':'SG Dashboard',
   
}
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} 
'''
DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.mysql",
        'NAME': "Myportfolio",
        'HOST': "myportfolio.cd53tbtkiw3v.ap-south-1.rds.amazonaws.com",
        'USER': "sgadmin",
        'PASSWORD': "Sai12345#",  # Or your host name if MySQL is on a different server
        'PORT': "3306", # Default MySQL port
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },  
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True



# AWS configaration 

AWS_ACCESS_KEY_ID = "AKIAXDOEKGCL6QK5VED5"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "myportfolio-django"
AWS_S3_SIGNATURE_NAME = "s3v4"
AWS_S3_REGION_NAME = "ap-south-1"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERITY = True

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# To security for deploy
'''
SECURE_HSTS_SECONDS = 31536000  # Set the HSTS max-age to a year (adjust as needed)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True 


'''