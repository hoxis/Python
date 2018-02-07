# coding=utf-8

from selenium import webdriver

url = 'http://www.heibanke.com/lesson/crawler_ex01/'

# browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser.get(url)

for i in range(31):
    username = browser.find_element_by_name('username')
    username.clear()
    username.send_keys('liuhaha')

    password = browser.find_element_by_id("id_password")
    password.clear()
    password.send_keys(i)
    # FireFox下异步，Chrome下同步，submit方法会等待页面加载完成后返回
    # password.submit()

    # 两种浏览器下click()方法都会等到加载完成后返回
    browser.find_element_by_id('id_submit').click()
    
    returnText = browser.find_element_by_tag_name('h3')
    print(returnText.text + ', password ' + str(i))
    if u"成功" in returnText.text:
        break
    browser.back()

browser.quit()
