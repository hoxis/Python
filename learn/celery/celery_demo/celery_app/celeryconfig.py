# 指定 Broker
BROKER_URL = 'redis://127.0.0.1:6379'
# 指定 Backend
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

# 指定时区，默认是 UTC
CELERY_TIMEZONE = 'Asia/Shanghai'

# 指定导入的任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2'
)
