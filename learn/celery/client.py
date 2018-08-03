# encoding=utf-8

from tasks import add

# 异步任务
add.delay(2, 8)

print('hello~')