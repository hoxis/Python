# coding=utf-8

import requests, bs4
import threading
import queue
import time
from threading import Thread


def getPassword(page):
    payload['page'] = page
    print('loading data from %s?page=%s ...' %(pwd_url, page))
    pwd_response = requests.get(pwd_url, cookies=cookies, params=payload)

    soup = bs4.BeautifulSoup(pwd_response.text, "html.parser")

    pwd_pos = soup.findAll('td', {'title':'password_pos'})
    pwd_value = soup.findAll('td', {'title':'password_val'})

    for index in range(len(pwd_pos)):
        pwd_data[int(pwd_pos[index].getText())] = pwd_value[index].getText()
    q.put('ok')
    print('now the pwd_data length is %s' % len(pwd_data))
    

# 通过观察，密码应该有100个数字组成。
# 由于每次获取到的密码会有重复，所以不是一次查询完就能获取到所有数字
# 这里一直进行查询，直到获取到100个数字
# while len(pwd_data) < 100:
#     # 因为每一页的密码位置都是随机给出的，其实这里可以不传page参数，一直调用pwd_url也可以获取到全部密码
    
#     for page in range(1,14):
#         if q.get():
#             t=threading.Thread(target=getPassword,args=(page,))
#             t.start()
#         if len(pwd_data)==100:
#             break


class MyThread(Thread):  
    def __init__(self, s):  
        Thread.__init__(self)  
        self.s = s  
      
    def run(self):  
        global count  
        global pwdlist  
        global exit  
        ruler = re.compile(r'.*>(\d*)<.*')  # 提取密码位置和值的正则表达式  
        while len(pwd_data) < 100:  
            pwd_response = requests.get(pwd_url, cookies=cookies)
            soup = bs4.BeautifulSoup(pwd_response.text, "html.parser")

            pwd_pos = soup.findAll('td', {'title':'password_pos'})
            pwd_value = soup.findAll('td', {'title':'password_val'})

            pwdpage = s.get(pwd_website).content  
            password_pos = BeautifulSoup(pwdpage, 'html.parser').findAll('td', {'title': 'password_pos'})  
            password_val = BeautifulSoup(pwdpage, 'html.parser').findAll('td', {'title': 'password_val'})  
            for index in range(len(pwd_pos)):
                pwd_data[int(pwd_pos[index].getText())] = pwd_value[index].getText()
            print('now the pwd_data length is %s' % len(pwd_data))
        if exit == 0:  
            exit = 1  
            print ''.join(pwdlist)  
              
if __name__ == '__main__':  
    start = time.time()
    payload = {}
    pwd_data = {}

    # 题目URL
    url = 'http://www.heibanke.com/lesson/crawler_ex03/'

    # 登录URL，获取cookie
    login_url = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex03/'

    # 获取密码URL
    pwd_url = 'http://www.heibanke.com/lesson/crawler_ex03/pw_list/'

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
    for i in range(0, 20):  # 线程数,可自定义  
        thread = MyThread(s)  
        thread.start()
    
    # 拼接password
    password = ''
    for key in sorted(pwd_data.keys()):
        password = password + pwd_data[key]
    print(password)

    # 重新登录
    playload = {'username':'liuhaha', 'password':password}
    playload['csrfmiddlewaretoken'] = cookies['csrftoken']

    r = requests.post(url, data=playload, cookies=cookies)

    print(u'执行结果：' + str(r.status_code))

    if r.status_code == 200:
        # print(r.text)
        if u"成功" in r.text:
            print(u'闯关成功！密码为：' + password)
            print(u'用时 %s s' % (time.time() - start))
            # break
    else:
        print(u'Failed')
        # break
