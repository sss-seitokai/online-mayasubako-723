"""
Django settings for online_meyasubako project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from .settings_local import *
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'meyasubako',
    'users',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'social_django', 
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
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'online_meyasubako.urls'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',  # OpenId用
    # 'social_core.backends.google.GoogleOpenId',  # Google OpenId用
    'social_core.backends.google.GoogleOAuth2',  # Google OAuth2用

    'social_core.backends.github.GithubOAuth2',  # Github用
    'social_core.backends.twitter.TwitterOAuth',  # Twitter用
    'social_core.backends.facebook.FacebookOAuth2',  # Facebook用

    'django.contrib.auth.backends.ModelBackend',  # デフォルトバックエンド、必須。
)

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

                'social_django.context_processors.backends',  # 追加
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'online_meyasubako.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


try:
    # 存在する場合、ローカルの設定読み込み
    from .settings_local import *
except ImportError:
    pass

if not DEBUG:
    # Heroku settings

    # staticの設定
    import os
    # import django-heroku


    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Static files (CSS, JavaScript, Images)
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    STATIC_URL = '/static/'

    # Extra places for collectstatic to find static files.
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    MIDDLEWARE += [
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ] 
    




import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
db_from_env = dj_database_url.config(conn_max_age=600,
ssl_require=True)
DATABASES['default'].update(db_from_env)
# try:
#  from ..local_settings import *
# except ImportError:
#  pass
if not DEBUG:
 SECRET_KEY = 'django-insecure-%cqnj&mh!1&z!w-$aj9nfn5dnnw#=g7dr(&0&2jan66(&m%ycu' #削除したSECRET_KEYをコピペします

import django_heroku
django_heroku.settings(locals())

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '894048995969-douuhpena6hkkvnbu1rk8knq0skal9mc.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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' 

SOCIAL_AUTH_URL_NAMESPACE = 'social'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'

MIDDLEWARE_CLASSES = ['social_django.middleware.SocialAuthExceptionMiddleware',]

ALLOWED_REDIRECT_URI_SCHEMES = ['http','https','social']