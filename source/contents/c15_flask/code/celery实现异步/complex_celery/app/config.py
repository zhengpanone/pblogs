class BaseConfig:
    CELERY_BROKER_URL = 'redis://localhost:6379/2'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
    CELERY_TASK_SERIALIZER = 'json'
