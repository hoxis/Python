# coding=utf-8

import requests
import bs4
import pytesseract
import re
from PIL import Image

def login():
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
    return login_response.cookies

def getImage():
    # 获取登录页面
    response = requests.get(url, cookies=cookies)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    # 解析获取图片地址
    image_url = 'http://www.heibanke.com' + soup.select('img[class="captcha"]')[0]['src']
    # print(soup.select('img[class="captcha"]')[0]['src'].split('/')[-2])
    # 获取图片
    image_response = requests.get(image_url)
    # if image_response.status_code != 200:
    # print('get image: ' + image_url)
    image = image_response.content
    # 保存图片
    with open('./crawler_ex04.png', 'wb') as f:
        f.write(image)
    
    code_typein = input('请根据下载图片 crawler_ex04.png 输入验证码：')
    return soup.select('img[class="captcha"]')[0]['src'].split('/')[-2], code_typein


if __name__ == '__main__':  
    url = 'http://www.heibanke.com/lesson/crawler_ex04/'
    login_url = 'http://www.heibanke.com/accounts/login'
    login_data = {'username':'liuhaha', 'password':'123456'}

    cookies = login()

    playload = {'username':'liuhaha', 'password':'1'}
    playload['csrfmiddlewaretoken'] = cookies['csrftoken']

    for i in range(100):
        captcha_0, captcha_1 = getImage()
        playload['captcha_0'] = captcha_0
        playload['captcha_1'] = captcha_1
        playload['password'] = i % 31
        # print(u'传入参数为：' + str(playload))

        r = requests.post(url, data=playload, cookies=cookies)
        soup = bs4.BeautifulSoup(r.text, "html.parser")

        # print(u'执行结果：' + str(r.status_code))

        if r.status_code == 200:
            if u"成功" in r.text:
                print(u'闯关成功！密码为：' + str(i%31))
                break
            else:
                print(u'密码%s不对，继续下一个' % (i%31))
        else:
            print(u'Failed')
            break