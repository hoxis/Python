# coding=utf-8

import requests

url = 'http://www.heibanke.com/lesson/crawler_ex02/'

login_url = 'http://www.heibanke.com/accounts/login'

login_data = {'username':'liuhaha', 'password':'123456'}

# 获取默认cookie
response = requests.get(url)
if response.status_code == 200:
    print('Welcome')
cookies = response.cookies

# 登录 
login_data['csrfmiddlewaretoken'] = cookies['csrftoken']
login_response = requests.post(login_url, allow_redirects=False, data=login_data, cookies=cookies)
if login_response.status_code == 200:
    print('login sucessfully')
# 获取登录成功后的cookie
cookies = login_response.cookies

playload = {'username':'liuhaha', 'password':'1'}
playload['csrfmiddlewaretoken'] = cookies['csrftoken']

for i in range(31):
    playload['password'] = i
    print(u'传入参数为：' + str(playload))

    r = requests.post(url, data=playload, cookies=cookies)

    # print(u'执行结果：' + str(r.status_code))

    if r.status_code == 200:
        if u"成功" in r.text:
            print(u'闯关成功！密码为：' + str(i))
            break
    else:
        print(u'Failed')
        break