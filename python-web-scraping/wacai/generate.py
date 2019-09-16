import requests, json, os
import csv
import uuid
import time
from bs4 import BeautifulSoup
import openpyxl
# import pandas as pd
import sys

import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

out_json = {}
in_json = {}

def get_type():
    soup = BeautifulSoup(open('支出类别.html', 'rb'), "lxml")
    list = soup.find_all(attrs={'onclick':'getSelected(event)'})
    for i in list:
        out_json[i.attrs['typeid']] = i.get_text()
    soup = BeautifulSoup(open('收入类别.html', 'rb'), "lxml")
    list = soup.find_all(attrs={'class':'normal cutlong'})
    for i in list:
        in_json[i.attrs['oid']] = i.attrs['name']

def get_bill(month):
    url = "https://jz.wacai.com/api/flow/bill/list"
    querystring = {"bookId":"xx","month":month}
    headers = {
        'x-access-token': "xx"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text)

def process(result):
    # 存放解析好的信息
    list_info = []
    datas = result.get('data')
    for data in datas:
        one_data = []
        updatedTime = data.get('updatedTime')
        time_local = time.localtime(int(updatedTime)/1000)
        # 将 UNIX 时间戳转化为普通时间格式
        updatedTime = time.strftime("%Y-%m-%d %H:%M", time_local)
        comment = data.get('comment')
        amount = data.get('amount')
        tip = data.get('tip')
        categoryId = data.get('categoryId')
        category = out_json.get(categoryId) if data.get('recType') == 1 else in_json.get(categoryId)
        recType = u'支出' if data.get('recType') == 1 else u'收入'
        one_data = [recType, updatedTime, category, amount, u'现金', tip + ' ' + comment]
        # print(one_data)
        list_info.append(one_data)
    return list_info

def file_do(list_info):
    # 获取文件大小
    if not os.path.exists('bill.csv' ):
        os.system(r'touch %s' % 'bill.csv')
    file_size = os.path.getsize(r'bill.csv')
    if file_size == 0:
        # 表头
        name = ['类型','时间','类别','金额','账户','备注']
        # 建立DataFrame对象
        file_test = pd.DataFrame(columns=name, data=list_info)
        # 数据写入
        file_test.to_csv(r'bill.csv',
                            encoding='utf-8', index=False)
    else:
        with open(r'bill.csv', 'a+', encoding="utf-8",newline='') as f:
            # 追加到文件后面
            writer = csv.writer(f)
            # 写入文件
            writer.writerows(list_info)

def file_do(list_info, file_name):
    # 获取文件大小
    if not os.path.exists(file_name):
        wb = openpyxl.Workbook()
        page = wb.active
        page.title = 'bill'
        page.append(['类型','时间','类别','金额','账户','备注'])
    else:
        wb = openpyxl.load_workbook(file_name)
        page = wb.active
    for info in list_info:
        page.append(info)
    wb.save(filename=file_name)

if __name__ == '__main__':
    file_name = str(uuid.uuid1()) + '.xlsx'
    get_type()
    start_year = 2017
    end_year = 2019

    for year in range(start_year, end_year+1):
        for month in range(1, 13):
            m = str(year) + ("%02d" % month)
            print(m)
            result = get_bill(m)
            processed_data = process(result)
            file_do(processed_data, file_name)
    print('data has saved in {}'.format(file_name))