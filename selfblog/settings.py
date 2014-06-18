#coding:utf-8
#TODO:增加Ueditor
#TODO:修改SHOW_TOOLBAR_CALLBACK，见http://django-debug-toolbar.readthedocs.org/en/1.2/configuration.html
import os
from os import path

# Debug setting
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Basic setting
ROOT_PATH = path.abspath(path.join(path.dirname('settings.py')))
ADMINS = (
    ('mush', 'btyh17mxy@gmail.com'),
)
MANAGERS = ADMINS
ALLOWED_HOSTS = ['localhost', 'mushapi.sinaapp.com']
# Different setting on local environment and SAE.
if 'SERVER_SOFTWARE' in os.environ:
    # Settings on SAE
    DEBUG = False
    DOMAIN = 'http://mushapi.sinaapp.com'
    DB_HOST = 'w.rdc.sae.sina.com.cn'
    DB_PORT = '3307'
    DB_USER = 'wjm330jzx2'
    DB_PASS = 'yjyjy0i5xy3z2xyzkkh4455h5ijzyi4zzmxm2lhx'
    DB_DB   = 'app_mushapi'
    CACHES_BACKEND = 'django.core.cache.backends.memcached.PyLibMCCache'
    UEDITOR_UPLOAD = {
        'BACKEND':'DjangoUeditor.saebackend',
        'DOMAIN':'mushapi',
    }
else:
    # Settings on Local environment
    DOMAIN = 'http://localhost:8000'
    CACHES_BACKEND = 'django.core.cache.backends.memcached.MemcachedCache'
    if DEBUG:
        DB_HOST = 'localhost'
        DB_PORT = ''
        DB_USER = 'root'
        DB_PASS = 'root'
        DB_DB   = 'selfblog'
    else:
        from sae._restful_mysql import monkey
        monkey.patch()

        DB_HOST = 'w.rdc.sae.sina.com.cn'
        DB_PORT = '3307'
        DB_USER = 'wjm330jzx2'
        DB_PASS = 'yjyjy0i5xy3z2xyzkkh4455h5ijzyi4zzmxm2lhx'
        DB_DB   = 'app_mushapi'


# Datebase Setting
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_DB,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}


# some django setting.
TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-cn'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
SECRET_KEY = 'm_t&=vit))7cic$zfdl^7wfsc+$e1@_p=4@bmc54pp%25n#*%1'


# Media, static files and template setting.
MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    path.join(ROOT_PATH, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_DIRS = (
    path.join(ROOT_PATH, 'templates'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)


# Middleware
MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pingback.middleware.PingbackMiddleware',
    'blog.middleware.OnlineMiddleware',
)


# Apps
INSTALLED_APPS = (
    'DjangoUeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.admin',
    'django.contrib.markup',
    'django_xmlrpc',
    'xadmin',
    'crispy_forms',
    'pingback',
    'duoshuo',
    'blog',
)


ROOT_URLCONF = 'selfblog.urls'
WSGI_APPLICATION = 'selfblog.wsgi.application'


# Pingback setting
DIRECTORY_URLS = (
    'http://ping.blogs.yandex.ru/RPC2',
    'http://rpc.technorati.com/rpc/ping',
)


# Logging setting
if DEBUG:
    INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar', )
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware', )
    LOG_FILE = '/tmp/blog.log'
else:
    LOG_FILE = '/tmp/blog.log'

LOGGING = {

}



# Debug_toolbar settings
DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
INTERNAL_IPS = ('127.0.0.1',)

# Caches setting
CACHES = {
    'default': {
        'BACKEND': CACHES_BACKEND,
        'LOCATION': 'unique-snowflake',
        'options': {
            'MAX_ENTRIES': 1024,
        }
    },
    'memcache': {
        'BACKEND': CACHES_BACKEND,
        'LOCATION': '127.0.0.1:11211',
        'options': {
            'MAX_ENTRIES': 1024,
        }
    },
}

# Blog setting
RESTRUCTUREDTEXT_FILTER_SETTINGS = {
    'doctitle_xform': False,
}

PAGE_NUM = 10
RECENTLY_NUM = 15
HOT_NUM = 15
ONE_DAY = 24*60*60
FIF_MIN = 15 * 60
FIVE_MIN = 5 * 60

# Duoshuo setting
DUOSHUO_SECRET = '6780677cb2b24d811b06dafbda1116fc'
DUOSHUO_SHORT_NAME = 'mushapi'

# 微信
WEIXIN_APPID = 0
WEIXIN_APPSECRET = ''
