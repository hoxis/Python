# coding=utf-8
'''
data : 20190917
author : 不正经程序员
goal : 数据的可视化
'''

# 导入Style类，用于定义样式风格
from pyecharts import Style
import json
# 导入Geo组件，用于生成柱状图
from pyecharts import Bar
# 导入Counter类，用于统计值出现的次数
from collections import Counter

import fileinput,re

# 设置全局主题风格
from pyecharts import configure
configure(global_theme='wonderland')

# 数据可视化
dates = []
comment_text = ""

def render():
    global comment_text
    with open('jay.csv', mode='r', encoding='utf-8') as f:
        rows = f.readlines()
        for row in rows[1:]:
            if row.count(',') != 3:
                continue
            elements = row.split(',')
            user = elements[0]
            date = elements[1]
            if '2019' not in date:
                continue
            like = elements[2]
            comment = elements[3]
            if '2019-09-14' in date:
                dates.append('2019-09-14')
            elif '2019-09-15' in date:
                dates.append('2019-09-15')
            elif '2019-09-16 0' in date or '2019-09-16 1' in date or '2019-09-16 20' in date or '2019-09-16 21' in date:
                dates.append('2019-09-16 0-21')
            elif '2019-09-18' in date:
                continue
            else:
                dates.append(date)
            comment_text += comment

    with open("comment_text.txt","w", encoding='utf-8') as f:
        f.write(comment_text)

    date_data = Counter(dates).most_common()
    # 按日期进行排序
    date_data = sorted(date_data)
    # print(data)

    # 根据评分数据生成柱状图
    bar = Bar('评价人数走势图', '数据来源：不正经程序员-采集自QQ音乐',
              title_pos='center', width=800, height=600)
    attr, value = bar.cast(date_data)
    bar.add('', attr, value, is_visualmap=False, visual_range=[0, 3500], visual_text_color='#fff', is_more_utils=True,
            xaxis_interval=0, xaxis_rotate=30,is_label_show=True,xaxis_label_textsize=8, label_text_size=8)

    bar.render(
        'picture\评价人数走势图.html')

render()
