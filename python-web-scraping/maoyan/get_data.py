# encoding=utf-8
'''
data : 2019-8-6
author : 不正经程序员
goal : 抓取猫眼数据
'''
import os
import csv
import random
import time
import datetime
import json
import requests
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# from fake_useragent import UserAgent

USER_AGENTS = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)", "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)", "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)", "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
               "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)", "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1", "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0", "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20", "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52", ]


class Spidermaoyan():
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Host": "m.maoyan.com",
                "Referer": "http://m.maoyan.com/movie/1211270/comments?_v_=yes"
    }

    def __init__(self, url):
        self.url = url

    # 发送get请求
    def get_json(self):
        # 发送get请求
        try:
            response_comment = requests.get(self.url, headers=self.headers)
        except Exception as err:
            print(err)
            return None
        json_comment = response_comment.text
        json_comment = json.loads(json_comment)
        # print(json_comment)
        return json_comment

    # 获取数据并存储
    def get_data(self, json_comment):
        json_response = json_comment["cmts"]  # 列表
        # print(json_response)
        print(len(json_response))
        list_info = []
        for data in json_response:
            cityName = data.get("cityName")
            content = data.get("content").replace("\r\n","").replace("\n","")
            if "gender" in data:
                gender = data.get("gender")
            else:
                gender = 0
            nickName = data.get("nickName")
            userLevel = data.get("userLevel")
            score = data.get("score")
            time = data.get("startTime")
            date = data.get("startTime").split()[0]
            list_one = [date, time, nickName, gender,
                        cityName, userLevel, score, content]
            list_info.append(list_one)
        # print(list_info)
        self.file_do(list_info)
        return data

    # 存储文件
    def file_do(self, list_info):
        # 获取文件大小
        file_size = os.path.getsize(r'maoyan.csv')
        if file_size == 0:
            # 表头
            name = ['date','time','name','gender','city','userLevel','score','content']
            # 建立DataFrame对象
            file_test = pd.DataFrame(columns=name, data=list_info)
            # 数据写入
            file_test.to_csv(r'maoyan.csv',
                             encoding='utf_8_sig', index=False)
        else:
            with open(r'maoyan.csv', 'a+') as file_test:
                # 追加到文件后面
                writer = csv.writer(file_test)
                # 写入文件
                writer.writerows(list_info)


def spider_maoyan():
    start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    end_time = '2019-07-20 00:00:00'
    offset = 0
    while start_time > end_time:
        comment_api = 'http://m.maoyan.com/mmdb/comments/movie/1211270.json?_v_=yes&offset=15&startTime=' + start_time.replace(' ', '%20')
        # comment_api = 'http://m.maoyan.com/mmdb/comments/movie/1211270.json?_v_=yes&offset={0}&startTime={1}%2021%3A09%3A31'.format(offset, startTime)
        s0 = Spidermaoyan(comment_api)
        while(True):
            json_comment = s0.get_json()
        if json_comment:
            break
        data = s0.get_data(json_comment)
        start_time = data.get("startTime")
        start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(seconds=-1)
        start_time = datetime.datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')
        offset = offset + 15
        # time.sleep(1)


if __name__ == '__main__':
    spider_maoyan()
