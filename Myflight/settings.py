"""
Django settings for Myflight project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
LOGIN_URL = '/Myflightadmin/login/'
APIKEY='5aa19590f824fcaf4a76f9039c812da6'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',# 缓存使用redis数据库储存
        'LOCATION': 'redis://127.0.0.1:6379/5',# 使用本地的6379端口(redis的默认端口)第五个数据库(redis共有16个数据库0-15)
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",# 使用django_redis的默认参数
        },
    },
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7k(oao7(t99l(3uz+klj8r-8@^z&_3a((aw%b3iklp!%92&0f4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['219.239.227.198','localhost']
ALLOWED_HOSTS = ['127.0.0.1','localhost','114.115.134.188']



# Application definition

INSTALLED_APPS = [
    # 'django_crontab',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
    'airplane',
    'airport',
    'login',
    'user',
    'Myflightadmin',
    'rest_framework',
    'web_session',
]

# CRONJOBS = [
#     # 表示每两分钟执行一次
#     ('*/1 * * * *', 'airplane.task.task'),
#     # ('*/2 * * * *', 'airplane.views.scan_trip'),
# ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Myflight.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Myflight.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
import pymysql         # 一定要添加这两行！通过pip install pymysql！
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Myflight',
        'HOST': '114.115.134.188',
        'USER': 'root',
        'PASSWORD': 'wodehangban',
        'PORT': '3306',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static") # 收集Django的静态文件到同一个static中
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "/static/"),
    BASE_DIR+"/user/"+"static/",
    BASE_DIR+"/Myflightadmin/"+"static/",

]

SESSION_COOKIE_NAME = "sessionid"       # Session的cookie保存在浏览器上时的key
SESSION_COOKIE_PATH = "/"               # Session的cookie保存的路径(默认)
SESSION_COOKIE_DOMAIN = None            # Session的cookie保存的域名(默认)
SESSION_COOKIE_SECURE = False           # 是否Https传输cookie
SESSION_COOKIE_HTTPONLY = True          # 是否Session的cookie只支持http传输(默认)
SESSION_COOKIE_AGE = 1209600            # Session的cookie失效日期(2周)(默认)
SESSION_SAVE_EVERY_REQUEST = False      # 是否设置关闭浏览器使得Session过期
SESSION_COOKIE_AT_BROWSER_CLOSE = False  # 是否每次请求都保存Session，默认修改之后才能保存