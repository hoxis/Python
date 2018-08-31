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
    # 获取图片
    image_response = requests.get(image_url)
    # if image_response.status_code != 200:
    print('get image: ' + image_url)
    image = image_response.content
    # 保存图片
    with open('./crawler_ex04.png', 'wb') as f:
        f.write(image)
    # 转为灰度图片
    image = Image.open('./crawler_ex04.png').convert('L')
    # 二值化
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = image.point(table, '1')
    return soup.select('img[class="captcha"]')[0]['src'].split('/')[-2], out

if __name__ == '__main__':  
    url = 'http://www.heibanke.com/lesson/crawler_ex04/'
    login_url = 'http://www.heibanke.com/accounts/login'
    login_data = {'username':'liuhaha', 'password':'123456'}

    cookies = login()

    playload = {'username':'liuhaha', 'password':'1'}
    playload['csrfmiddlewaretoken'] = cookies['csrftoken']

    # 这里因为识别率低，循环了 10000 次。。。
    for i in range(10000):
        optCode = ''
        # 若解析处理的验证码长度不为4或者包含其他非英文字符，则继续获取
        while not (len(optCode) == 4 and re.findall("[ACDEFGHJKLMPQTVWXYZadefghklptxyz]{4}", optCode)):
            # 识别验证码
            captcha_0, image = getImage()
            optCode = pytesseract.image_to_string(image, lang="eng", config="--psm 7")
            # 验证码的准确率是个问题啊
            print(u'解析到的验证码为：' + optCode)

        playload['captcha_0'] = captcha_0
        playload['captcha_1'] = optCode
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