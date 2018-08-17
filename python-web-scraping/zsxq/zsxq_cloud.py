# encoding:utf-8

import requests
import json
import jsonpath
import datetime
import argparse
import jieba
import re
import os
import sys
import numpy
from PIL import Image
from wordcloud import WordCloud


# 命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--day', type=str, help="input the day time, like 2018-06-14", default=(datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d'))   # 哪一天的数据

# 获取参数
args = parser.parse_args()
DAY = args.day

url = "https://api.zsxq.com/v1.10/groups/2421112121/topics"
authorization = "851754EE-18AE-F296-4FA7-D55ADCA10435"
headers = {
    'authorization': authorization,
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    'x-request-id': "14a410ef-6756-4fc8-9671-ce2a699f9b5c",
    'connection': "keep-alive",
    'origin': "https://wx.zsxq.com",
    'host': "api.zsxq.com",
    'x-version': "1.10.0",
    'accept': "application/json, text/plain, */*",
    'referer': "https://wx.zsxq.com/dweb/",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    'cache-control': "no-cache",
    'postman-token': "a5d2672a-8994-4c60-b20b-bd684afcf239"
}

# 获取某一个小时内的数据
# 传入时间格式为：2018-18-29 20
def get_hour_data(source_time):
    result = ""
    
    # 若传入的时间超出当前时间，则直接返回空值
    if source_time > datetime.datetime.now():
        return result
    # 时间格式化
    end_time = source_time.strftime('%Y-%m-%dT%H') + ":00:00.000+0800"
    temp_time = source_time - datetime.timedelta(hours=1)
    begin_time = temp_time.strftime('%Y-%m-%dT%H') + ":00:00.000+0800"
    querystring = {"count": "20", "end_time": end_time, "begin_time": begin_time}
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)
    # 获取异常时直接退出
    # 异常时会返回一个 code
    if 'code' in result and result['code'] != 200:
        print('Get data failed. Please check the parameters')
        sys.exit(1)
    return result

def parse_data(result):
    text = ""
    # 若当前时间没有主题发布，获取到的 topics 会是一个空的嵌套 list： [[]]
    if len(jsonpath.jsonpath(result, "$..topics")[0]) != 0:
        # 利用 jsonpath 解析目标
        text_list = jsonpath.jsonpath(result, "$..topics[*]..text")
        for t in text_list:
            text += t
    return text

# 删除其中的标签内容
def filter_data(text):
    reg = re.compile('<[^>]*>')
    content = reg.sub(u'',text)
    return content

# 获取某一天的数据
def get_day_data(one_time):
    pass

if __name__ == "__main__":
    with open('result.txt', 'w+') as f:
        for i in range(24):
            time = DAY + " " + str(i)
            temp_time = datetime.datetime.strptime(time, '%Y-%m-%d %H')
            result = get_hour_data(temp_time)
            if result:
                data = parse_data(result)
                result = filter_data(data)
                f.write(result)
    
    # 若没有采集到数据则直接退出
    if os.path.getsize('result.txt'):
        # jieba 分词
        f = open('result.txt').read()
        wordlist = jieba.cut(f, cut_all=True)
        wl_space_split = " ".join(wordlist)

        coloring = numpy.array(Image.open("python.png"))

        # width,height,margin 可以设置图片属性
        # generate 可以对全部文本进行自动分词，但是他对中文支持不好，所以这里我们使用 jieba 先进行了分词
        # 通过 font_path 参数来设置字体集
        # 通过 mask 参数 来设置词云形状
        my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=coloring, 
                        font_path='fangsong_GB2312.ttf', max_font_size=50, random_state=42).generate(wl_space_split)
        my_wordcloud.to_file('test.png')
    else:
        print('get nothing, please check the parameters')
    # 删除临时文本文件
    os.unlink('result.txt')
