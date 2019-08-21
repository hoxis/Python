# encoding=utf-8
'''
data : 2019-8-6
author : 不正经程序员
goal : 抓取猫眼数据
'''
import datetime
import json
import random
import requests
import pandas as pd

USER_AGENTS = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)", "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)", "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)", "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
               "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)", "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1", "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0", "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20", "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52", ]


class Piao():
    def __init__(self, date, piaofang, paipianbi,shangzuolv):
        self.date = date
        self.piaofang = piaofang
        self.paipianbi = paipianbi
        self.shangzuolv = shangzuolv

def get_piaofang_info(date, movie_name):
    url = "https://box.maoyan.com/promovie/api/box/second.json"

    querystring = {"beginDate":date}

    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': "*/*",
        'Host': "box.maoyan.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        temp = json.loads(response.text)
        if temp:
            info_list = temp['data']['list']
            for info in info_list:
                if info['movieName'] == movie_name:
                    return Piao(date.replace('2019',''), info['boxInfo'], info['boxRate'].replace('%',"").replace('<',''), info['avgSeatView'].replace('%',""))
    return Piao(date, -1,-1,-1)

if __name__ == '__main__':
    list_info = []
    start_date = datetime.datetime.strptime("20190809", '%Y%m%d')
    end_date = datetime.date.today()
    while start_date.date() < end_date:
        piao = get_piaofang_info(start_date.strftime('%Y%m%d'), "上海堡垒")
        list_one = [piao.date, piao.piaofang, piao.paipianbi, piao.shangzuolv]
        list_info.append(list_one)
        start_date = start_date + datetime.timedelta(days = 1)
        # # 追加到文件后面
        # writer = csv.writer(f)
        # # 写入文件
        # writer.writerow(piao.date, piao.piaofang,)

    name = ['date','piaofang','paipianbi','shangzuolv']
    # 建立DataFrame对象
    file_test = pd.DataFrame(columns=name, data=list_info)
    # 数据写入
    file_test.to_csv(r'piaofang.csv',
                        encoding='utf_8_sig', index=False)