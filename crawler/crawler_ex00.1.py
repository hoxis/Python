# --coding=utf-8--

import re
from selenium import webdriver

url = 'http://www.heibanke.com/lesson/crawler_ex00/'

browser = webdriver.Firefox()

while True:
    # download the page
    print("Forward to page %s ..." % url)
    browser.get(url)
    elem = browser.find_element_by_tag_name('h3')

    # get the url of the for the next page
    print(elem.text)
    number = re.findall("\d+", elem.text)
    if number == []:
        print('The end.')
        browser.quit()
        break;
    else:
        url = 'http://www.heibanke.com/lesson/crawler_ex00/' + number[0] # 拼接新地址