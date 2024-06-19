"""
Django settings for final project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import environ
from environ import Env


# 사용법 : {App 이름}.{Model 이름}
AUTH_USER_MODEL = "users.User"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# django-environ 라이브러리를 활용한 지정, 경로의 .env 내역을 환경변수로서 로딩
env = environ.Env()

env_path = BASE_DIR / ".env"

if env_path.is_file():
    with env_path.open('rt', encoding='utf-8') as f:
        env.read_env(f, overwrite=True)

if env_path.exists():
    with env_path.open(encoding="utf8") as f:
        # 디폴트동작으로 동일 이름의 환경변수가 이미 등록된 경우, 덮어쓰기 하지 않음
        env.read_env(f, overwrite=True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-eqe^-+*paj08w9gn%z*w1g5o$zfntye91!yf(miw^ea(4tw(&-')
SECRET_KEY = os.environ['SECRET_KEY']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', 1))

if os.environ.get('DJANGO_ALLOWED_HOSTS'):
    ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(' ')
else:
    ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "channels",
    "daphne",
    "django_bootstrap5",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "sleep",
    "users",
    "app",
    "chat",
    "dr",
    "survey",
    "blogs",
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

ROOT_URLCONF = 'final.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'final.wsgi.application'

# asgi.py 부모 폴더명으로 '프로젝트' 변경
ASGI_APPLICATION = "final.asgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# CHANNEL_LAYER_REDIS_URL 환경변수가 설정되어있다면 로딩/파싱하여, CHANNEL_LAYERS 값을 설정
if "CHANNEL_LAYER_REDIS_URL" in env:
    channel_layer_redis = env.db_url("CHANNEL_LAYER_REDIS_URL")
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [
                    {
                        "host": channel_layer_redis["HOST"],
                        "port": channel_layer_redis.get("PORT") or 6379, # PORT 값이 거짓일 경우 (빈문자열, 0), 디폴트 포트번호로서 6379를 사용
                        "password": channel_layer_redis["PASSWORD"],
                    },
                ],
            },
        },
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login 성공시 URL 경로
LOGIN_REDIRECT_URL = "/"

# Logout 성공시 URL 경로
LOGOUT_REDIRECT_URL = "/"

OPENAI_API_KEY = env.str("OPENAI_API_KEY")

BOOTSTRAP5 = {
    "required_css_class": "fw-bold",
    "set_placeholder": False,
}

TAILWIND_APP_NAME = "theme"