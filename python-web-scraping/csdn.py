# --coding=utf-8--
#! python3

import requests, bs4
import re

def login():
    # 登录URL，获取cookie
    login_url = 'https://passport.csdn.net/account/login'
    login_data = {'username':'uuu', 'password':'123456'}

    response = requests.get(login_url)

    soup = bs4.BeautifulSoup(response.text, "html.parser")

    login_data['lt'] = soup.find('input', {'name':'lt'})['value']
    login_data['execution'] = soup.find('input', {'name':'execution'})['value']
    login_data['_eventId'] = 'submit'

    # print(login_data)

    # 登录 
    login_response = requests.post(login_url, allow_redirects=False, data=login_data, cookies=response.cookies)
    # print(login_response.text)
    if login_response.status_code == 200:
        print('login sucessfully')

    return login_response.cookies

def comment(sourceid, cookies):
    comment_url = 'http://download.csdn.net/index.php/comment/post_comment\
                    ?jsonpcallback=jQuery1709916717009362624_1519351091445&\
                    content=还不错，可以使用&txt_validcode=undefined&\
                    rating=4&t=1519351107193&_=1519351107194&sourceid=' + sourceid
    print('正在评价资源 %s' %sourceid)
    # print(comment_url)
    response = requests.get(comment_url, cookies=cookies)
    # print(response.text)

if __name__ == '__main__':  
    # 网站base URL
    base_url = 'http://download.csdn.net/'
   
    # 获取登录成功后的cookie
    cookies = login()

    # 获取尾页
    url = base_url + 'my/downloads';
    r = requests.get(url, cookies=cookies)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    element = soup.find("a", text="尾页")
    href = element['href']
    last_page = int(href.split('/')[-1])

    for page in range(1, last_page+1):
        url = base_url + 'my/downloads/' + str(page);
        print(url)
        r = requests.get(url, cookies=cookies)

        if r.status_code == 200:
            print('开始评价第 %s 页' %page)
            soup = bs4.BeautifulSoup(r.text, "html.parser")

            elements = soup.find_all("a", text="立即评价")
            
            for element in elements:
                href = element['href']
                # print(href)
                # 解析出资源ID
                sourceid = (href.split('/')[-1]).split('#')[0]
                comment(sourceid, cookies)
        else:
            # print(u'Failed')
            break
    print('已完成所有评价')
