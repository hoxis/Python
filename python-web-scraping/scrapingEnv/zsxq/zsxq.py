# encoding:utf-8

import requests
import json
import jsonpath
import time
import datetime
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--time', type=str, help="input the day time, like 2018-06-14", default=(datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d'))   # 哪一天的数据

# 获取参数
args = parser.parse_args()
DAY = args.time

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
    # 时间格式化
    end_time = source_time.strftime('%Y-%m-%dT%H') + ":00:00.000+0800"
    temp_time = source_time - datetime.timedelta(hours=1)
    begin_time = temp_time.strftime('%Y-%m-%dT%H') + ":00:00.000+0800"
    querystring = {"count": "20", "end_time": end_time, "begin_time": begin_time}
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)
    return result

def parse_data(result):

    return_data = {}
    # 若当前时间没有主题发布，获取到的 topics 会是一个空的嵌套 list： [[]]
    # 这里需要进行判断过滤
    if len(jsonpath.jsonpath(result, "$..topics")[0]) != 0:

        # print(result["resp_data"])
        # 利用 jsonpath 解析目标
        topic_id_list = jsonpath.jsonpath(result, "$..topics[*].topic_id")
        create_time_list = jsonpath.jsonpath(result, "$..topics[*].create_time")
        comments_count_list = jsonpath.jsonpath(result, "$..topics[*].comments_count")
        likes_count_list = jsonpath.jsonpath(result, "$..topics[*].likes_count")
        name_list = jsonpath.jsonpath(result, "$..topics[*]...name")
        text_list = jsonpath.jsonpath(result, "$..topics[*]..text")
        # print(name_list)

        data = []

        for i, topic_id in enumerate(topic_id_list):
            item = {}
            item['topic_id'] = topic_id
            item['create_time'] = create_time_list[i]
            item['comments_count'] = comments_count_list[i]
            item['likes_count'] = likes_count_list[i]
            item['name'] = name_list[i]
            item['text'] = text_list[i]
            data.append(item)
        
        # 返回详情、总点赞数、总评论数、总主题数
        return_data = {}
        return_data['data'] = data
        return_data['total_like_count'] = sum(likes_count_list)
        return_data['total_comments_count'] = sum(comments_count_list)
        return_data['total'] = len(topic_id_list)

    return return_data


# 获取某一天的数据
def get_day_data(one_time):
    pass


if __name__ == "__main__":
    day_data = {}

    for i in range(24):
        time = DAY + " " + str(i)
        temp_time = datetime.datetime.strptime(time, '%Y-%m-%d %H')
        result = get_hour_data(temp_time)
        day_data[temp_time.strftime('%Y-%m-%d %H')] = parse_data(result)
    
    # 对用户发表内推词云分析
    for key, value in day_data.items():
        print(value)
    # print(list(day_data.values))
