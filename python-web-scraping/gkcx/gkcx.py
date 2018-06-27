# encoding:utf-8

from bs4 import BeautifulSoup
import requests
import json

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}



def get_school_id(school_name):
    Referer = "https://gkcx.eol.cn/soudaxue/queryschool.html?&keyWord1={}".format(school_name)
    data_url = "https://data-gkcx.eol.cn/soudaxue/queryschool.html"
    params = {
        "messtype" : "jsonp",
        "_":"1530074932531",
        "keyWord1" : school_name
    }
    headers["Referer"] = Referer.encode('utf-8')

    response = requests.request("GET", data_url,headers=headers,params=params)
    print(response.text)
    print(type(response.text))
    # j = json.eval(response.text)
    # print(j)

if __name__ == "__main__":
    # school_name = input("Please the school name：")
    school_name = '南京邮电大学'
    get_school_id(school_name)