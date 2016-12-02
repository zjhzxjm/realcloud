from .django_settings import *

INSTALLED_APPS += (
    # 'corsheaders',
    'wooey',
)

# MIDDLEWARE_CLASSES = [[i] if i == 'django.middleware.common.CommonMiddleware' else ['corsheaders.middleware.CorsMiddleware',i] for i in MIDDLEWARE_CLASSES]
MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
MIDDLEWARE_CLASSES.append('realcloud.middleware.ProcessExceptionMiddleware')

PROJECT_NAME = "realcloud"
WOOEY_CELERY_APP_NAME = 'wooey.celery'
WOOEY_CELERY_TASKS = 'wooey.tasks'
