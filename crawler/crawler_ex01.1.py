# coding=utf-8
import requests

url = 'http://www.heibanke.com/lesson/crawler_ex01/'

playload = {'username': 'liuhaha', 'password': '1'}

for i in range(31):
    playload['password'] = i
    print(u'传入参数为：' + str(playload))

    r = requests.post(url, data=playload)

    if u"成功" in r.text:
        print(u'闯关成功！')
        break