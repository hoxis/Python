# encoding=utf-8

import time
from celery import Celery

broker = 'redis://127.0.0.1:6379'
backend = 'redis://127.0.0.1:6379/0'

app = Celery('my_task', broker=broker, backend=backend)

@app.task
def add(x, y):
    # 模拟耗时操作
    time.sleep(5)
    return x + y