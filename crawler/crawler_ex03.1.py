# coding=utf-8

import requests, bs4
import threading
import time

def login():
    # 登录URL，获取cookie
    login_url = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex03/'
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

    return login_response.cookies

def getPassword(page):
    global pwd_data
    payload['page'] = page
    print(threading.currentThread().getName() + ', loading %s?page=%s ...' %(pwd_url, page))
    pwd_response = requests.get(pwd_url, cookies=cookies, params=payload)

    soup = bs4.BeautifulSoup(pwd_response.text, "html.parser")

    pwd_pos = soup.findAll('td', {'title':'password_pos'})
    pwd_value = soup.findAll('td', {'title':'password_val'})

    for index in range(len(pwd_pos)):
        pwd_data[int(pwd_pos[index].getText())] = pwd_value[index].getText()
    print(threading.currentThread().getName() + ', now the pwd_data length is %s' % len(pwd_data))
    
class MyThread(threading.Thread):  
    def __init__(self, s):  
        threading.Thread.__init__(self)
        self.s = s  
      
    def run(self):  
        global pwd_data
        global count
        while len(pwd_data) < 100:
            count += 1
            print('The sub-thread has run %s times' % count)
            getPassword(count % 13)
              
if __name__ == '__main__':  
    start = time.time()
    payload = {}
    # 存放密码键值对
    pwd_data = {}
    # 记录运行次数
    count = 0

    # 题目URL
    url = 'http://www.heibanke.com/lesson/crawler_ex03/'
     # 获取密码URL
    pwd_url = 'http://www.heibanke.com/lesson/crawler_ex03/pw_list/'
   
    # 获取登录成功后的cookie
    cookies = login()

    threads = []
    for i in range(0, 5):  # 线程数,可自定义  
        thread = MyThread(cookies)
        threads.append(thread)
        thread.start()
    
    # 等待所有线程完成
    for thread in threads:
        thread.join()
    
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
