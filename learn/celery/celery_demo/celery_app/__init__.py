# encoding=utf-8

from celery import Celery

# 创建 Celery 实例
app = Celery('demo')
# 通过 Celery 实例加载配置模块
app.config_from_object('celery_app.celeryconfig')
