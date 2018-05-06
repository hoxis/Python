#!/usr/bin/env python3
import pika

print("简单的向队列中加入消息")
# 创建连接对象
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.151.7'))
# 创建频道对象
channel = connection.channel()
# 指定一个队列，如果该队列不存在则创建
channel.queue_declare(queue='test_queue')
# 提交消息
for i in range(10):
    channel.basic_publish(
        exchange='', routing_key='test_queue', body='hello,world' + str(i))
    print("sent...")
# 关闭连接
connection.close()

print("从队列中获取消息")
credentials = pika.PlainCredentials('guest', 'guest')
# 连接到RabbitMQ服务器
connection = pika.BlockingConnection(
    pika.ConnectionParameters('192.168.151.18', 5672, '/', credentials))
channel = connection.channel()
# 指定一个队列，如果该队列不存在则创建
channel.queue_declare(queue='test_queue')
# 定义一个回调函数


def callback(ch, method, properties, body):
    print(body.decode('utf-8'))


# 告诉RabbitMQ使用callback来接收信息
channel.basic_consume(callback, queue='test_queue', no_ack=False)
print('waiting...')
# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理。按ctrl+c退出。
channel.start_consuming()
