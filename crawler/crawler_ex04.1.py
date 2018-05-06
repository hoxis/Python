# coding=utf-8

# 使用百度 OCR

import requests
import bs4
import pytesseract
import re
import time
from PIL import Image
from aip import AipOcr
from datetime import datetime
from shutil import copyfile

APP_ID = "11075466"
API_KEY = "5cjKbYlAsQDLTqoIucCrMGAC"
SECRET_KEY = "NHAAcE4igms1AFXXAMyIxZOzVmAR0zbb"

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
    with open('./crawler_ex04.png', "rb") as fp:
        return fp.read()

if __name__ == '__main__':  
    url = 'http://www.heibanke.com/lesson/crawler_ex04/'
    login_url = 'http://www.heibanke.com/accounts/login'
    login_data = {'username':'liuhaha', 'password':'123456'}

    cookies = login()

    playload = {'username':'liuhaha', 'password':'1'}
    playload['csrfmiddlewaretoken'] = cookies['csrftoken']

    for i in range(100):
        optCode = ''
        # 若解析处理的验证码长度不为4或者包含其他非英文字符，则继续获取
        while not (len(optCode) == 4 and re.findall("[a-zA-Z]{4}", optCode)):
            # 识别验证码
            OCR = AipOcr(APP_ID, API_KEY, SECRET_KEY)
            try:
                options = {}
                options["language_type"] = "ENG"
                respon = OCR.basicGeneral(getImage(), options)
                print(respon)
            except:
                print("error: baidu ocr error")
                time.sleep(3)
                sys.exit()
            optCode = (respon["words_result"][0])["words"]
            # optCode = pytesseract.image_to_string(getImage(), lang="500", config="-psm 7")
            # 验证码的准确率是个问题啊
            print(u'解析到的验证码为：' + optCode)

        playload['captcha_1'] = optCode
        playload['password'] = i % 31
        # print(u'传入参数为：' + str(playload))

        r = requests.post(url, data=playload, cookies=cookies)
        soup = bs4.BeautifulSoup(r.text, "html.parser")

        # print(u'执行结果：' + str(r.status_code))
        # print(r.text)

        if r.status_code == 200:
            if u"验证码输入错误" not in r.text:
                print(u'闯关成功！密码为：' + str(i%31))
                print(r.text)
                break
            else:
                print(u'密码%s不对，继续下一个' % (i%31))
        else:
            print(u'Failed')
            break