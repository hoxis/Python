# --coding=utf-8--
#! python3

import requests, bs4, re

url = 'http://www.heibanke.com/lesson/crawler_ex00/'

while True:
    # download the page
    print("forward to page %s ..." % url)
    response = requests.get(url)
    print("the return code : " + str(response.status_code))

    soup = bs4.BeautifulSoup(response.text, "html.parser")

    # get the url of the for the next page
    comic = soup.select('h3') # 获取页面数字
    print(comic[0].getText())
    number = re.findall("\d+", comic[0].getText())
    if number == []:
        print('The end.')
        break;
    else:
        url = 'http://www.heibanke.com/lesson/crawler_ex00/' + number[0] # 拼接新地址