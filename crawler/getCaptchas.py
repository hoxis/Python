# coding=utf-8

import requests
import bs4
import os

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

def getImage(image_name):
    # 获取登录页面
    response = requests.get(url, cookies=cookies)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    # 解析获取图片地址
    image_url = 'http://www.heibanke.com' + soup.select('img[class="captcha"]')[0]['src']
    # image_name = soup.select('img[class="captcha"]')[0]['src'].split('/')[-2]
    # 获取图片
    image_response = requests.get(image_url)
    if image_response.status_code != 200:
        print('get image fail: ' + image_url)
    image = image_response.content
    # 保存图片
    with open('./captchas/'+ str(image_name) +'.png', 'wb') as f:
        f.write(image)
    print('down image %s success' % image_name)

if __name__ == '__main__':  
    os.makedirs("captchas", exist_ok=True)
    url = 'http://www.heibanke.com/lesson/crawler_ex04/'
    login_url = 'http://www.heibanke.com/accounts/login'
    login_data = {'username':'liuhaha', 'password':'123456'}

    cookies = login()

    playload = {'username':'liuhaha', 'password':'1'}
    playload['csrfmiddlewaretoken'] = cookies['csrftoken']

    for i in range(50):
        getImage(i)
