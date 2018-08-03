# encoding=utf-8

from celery_app import task1
from celery_app import task2

# 也可用 task1.add.delay(2, 8)
task1.add.apply_async(args=[2, 8])

# 也可用 task2.multiply.delay(3, 7)
task2.multiply.apply_async(args=[3, 8])

print('hello')