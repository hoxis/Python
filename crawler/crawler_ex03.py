# coding=utf-8

import requests, bs4, time

start = time.time()

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

# TODO 解析最大页数

payload = {}
pwd_data = {}
i = 0
# 通过观察，密码应该有100个数字组成。
# 由于每次获取到的密码会有重复，所以不是一次查询完就能获取到所有数字
# 这里一直进行查询，直到获取到100个数字
while len(pwd_data) < 100:
    # 因为每一页的密码位置都是随机给出的，其实这里可以不传page参数，一直调用pwd_url也可以获取到全部密码
    payload['page'] = i % 13
    pwd_url = 'http://www.heibanke.com/lesson/crawler_ex03/pw_list/'
    print('------------------------')
    print('loading data from %s?page=%s ...' %(pwd_url, i%13))
    pwd_response = requests.get(pwd_url, cookies=cookies, params=payload)

    soup = bs4.BeautifulSoup(pwd_response.text, "html.parser")

    # 获取表格
    table = soup.select('[class="table table-striped"]')

    # 解析表格数据，过滤掉表头
    temp_data = {}
    for tr in table[0].find_all('tr')[1:]:
        tds = tr.find_all('td')
        # 分别取出password的位置及其对应的数字
        pwd_data[int(tds[0].getText())] = tds[1].getText()
        temp_data[int(tds[0].getText())] = tds[1].getText()
    # print(temp_data)
    i = i + 1
    print('The load has run %s times and now the pwd_data length is %s' % (i, len(pwd_data)))
        
# print(pwd_data)
# print('The length of password is %s.' % len(pwd_data))

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