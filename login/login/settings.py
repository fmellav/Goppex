"""
Django settings for login project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuraciones de seguridad
# SECURE_SSL_REDIRECT = False # con esto se redirige automaticamente las solicitudes HTTP a HTTPS, cifrando las comunicaciones entre cliente y servidor.
# CSRF_COOKIE_SECURE = False # las cookie de proteccion CSRF (Cross-Site Request Forgery) solo se transmiten mediante conexiones HTTPS, previene que se filtren las cookies en conexiones inseguras
# SESSION_COOKIE_SECURE = False # lo mismo que la de arriba pero aplica a las cookie de inicio de sesion
# SECURE_BROWSER_XSS_FILTER = False # Previene contra ataques XSS (Cross-Site Scripting) en navegadores modernos, ayudando a prevenir la ejecucion de scripts maliciosos en el navegador del usuario
# SECURE_CONTENT_TYPE_NOSNIFF = False # con esto se previene que el navegador intente adivinar el contenido de una respuesta, o sea, protege contra ataques de inyecciones de contenido


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-50cc)mkmgh_c0ki6_8lb*(!gyt)=@1cdozic6j^635ljlj7drx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Registro de intentos de accesos no autorizados
#   se guardan los instentos de acceso en un archivo para ser revisados
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'WARNING',
#             'class': 'logging.FileHandler',
#             'filename': 'django_security.log',
#         },
#     },
#     'loggers': {
#         'django.security': {
#             'handlers': ['file'],
#             'level': 'WARNING',
#             'propagate': True,
#         },
#     },
# }


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # Configura HTTPS, HSTS, entre otros.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # protege contra CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # previene Clickjacking
]

ROOT_URLCONF = 'login.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'login' / 'templates'],
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

WSGI_APPLICATION = 'login.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'usuarios',
        'USER': 'admin',
        'PASSWORD': 'QfZnGerT50.',
        'HOST': 'database-1.ctaa8oy2wvj6.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static",]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
