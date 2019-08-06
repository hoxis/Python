# coding=utf-8
'''
data : 2019-8-6
author : 不正经程序员
goal : 用于爬取数据的情感分析
'''

import fileinput,re
import requests, json

def is_float(str):
    try:
        float(str)
    except:
        return False
    else:
        return True

# 情感结果分析
def process_file():
    with open('D:\code\Python\python-web-scraping\maoyan\maoyan.csv', mode='r', encoding='utf-8') as f, open('D:\code\Python\python-web-scraping\maoyan\maoyan2.csv', mode='w', encoding='utf-8') as output_file:
        rows = f.readlines()
        for line in rows:
            if line.strip('\n') == 'date,time,name,gender,city,userLevel,score,content':
                output_file.write(line.strip('\n') + ',sentiment,positive_prob' + '\n')
                continue
            # 忽略逗号个数不规范的条目
            if line.count(',') != 7 and line.count(',') != 9:
                # print(line)
                continue
            elements = line.split(',')
            if len(elements) == 8:
                # 去除 除了中文、数字、字母之外的字符，防止json解析失败
                comment = re.sub('[^A-Za-z0-9\u4e00-\u9fa5]', '', elements[7])
                if comment != '':
                    # 获取情感分析结果
                    sentiment, positive_prob = sentiment_classify_tencentcloud(comment)
                    output_file.write(line.strip('\n') + ',' + sentiment + ',' + str(positive_prob) + "\n")
                    continue
            elif len(elements) == 10:
                if elements[8] == '-1':
                    comment = re.sub('[^A-Za-z0-9\u4e00-\u9fa5]', '', elements[7])
                    if comment != '':
                        # 获取情感分析结果
                        sentiment, positive_prob = sentiment_classify_tencentcloud(comment)
                        output_file.write(line.strip('\n') + ',' + sentiment + ',' + str(positive_prob) + "\n")
                        continue
                elif not is_float(elements[9]):
                    continue
                output_file.write(line)
                continue
            else:
                continue

def sentiment_classify_tencentcloud(text):
    from tencentcloud.common import credential
    from tencentcloud.common.profile.client_profile import ClientProfile
    from tencentcloud.common.profile.http_profile import HttpProfile
    from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
    from tencentcloud.nlp.v20190408 import nlp_client, models 
    try: 
        cred = credential.Credential("your_secret_id", "your_secret_key") 
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile) 

        req = models.SentimentAnalysisRequest()
        params = '{"Flag":2,"Text": \"' + text[:180] + '\"}'
        # params = '{"Flag":2,"Text":"好的"}'
        req.from_json_string(params)

        resp = client.SentimentAnalysis(req) 
        json_data = json.loads(resp.to_json_string())
        return json_data['Sentiment'],   round(float(json_data['Positive']),2)
        # print(resp.to_json_string()) 

    except TencentCloudSDKException as err: 
        print(err) 
        print(text)
        

process_file()