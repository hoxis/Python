# encoding=utf-8

import re
import requests
import json
import os
import pdfkit
from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib.parse import unquote

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
<h1>{title}</h1>
<p>{text}</p>
</body>
</html>
"""
htmls = []
num = 0
def get_data(url):

    global htmls, num
        
    headers = {
        'Authorization': 'FDAF90F0-3BDE-CCC6-1A7E-276C9148BA2D',
        'x-request-id': "7b898dff-e40f-578e-6cfd-9687a3a32e49",
        'accept': "application/json, text/plain, */*",
        'host': "api.zsxq.com",
        'connection': "keep-alive",
        'referer': "https://wx.zsxq.com/dweb/",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    }
    
    rsp = requests.get(url, headers=headers)
    # 将返回数据写入 jinghua.json 方便查看
    with open('jinghua.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(rsp.json(), indent=2, ensure_ascii=False))
    
    with open('jinghua.json', encoding='utf-8') as f:
        for topic in json.loads(f.read()).get('resp_data').get('topics'):
            content = topic.get('question', topic.get('talk', topic.get('task', topic.get('solution'))))
            
            # 对文本进行 URL 解码，要不后面解析处理也无法点击
            text = unquote(content.get('text', ''))

            # 星球中用 <e> 表示超链接
            # 这里我们进行转换
            soup = BeautifulSoup(text,"html.parser")
            links = soup.find_all('e', attrs={'type':'web'})
            if len(links):
                for link in links:
                    title = link.attrs['title']
                    href = link.attrs['href']
                    s = '<a href={}>{} </a>'.format(href,title)
                    text += s
            
            # 清理原文中的 <e> 标签
            # 这里不清理也没问题，HTML 解析不了，页面也不会显示
            # 但是，强迫症。
            text = re.sub(r'<e[^>]*>', '', text).strip()

            # 截取正文内容作为标题
            title = str(num) + text[:9]
            num += 1

            if content.get('images'):
                soup = BeautifulSoup(html_template, 'html.parser')
                for img in content.get('images'):
                    url = img.get('large').get('url')
                    img_tag = soup.new_tag('img', src=url)
                    soup.body.append(img_tag)
                    html_img = str(soup)
                    html = html_img.format(title=title, text=text)
            else:
                html = html_template.format(title=title, text=text)

            if topic.get('question'):
                answer = topic.get('answer').get('text', "")
                soup = BeautifulSoup(html, 'html.parser')
                answer_tag = soup.new_tag('p')
                answer_tag.string = answer
                soup.body.append(answer_tag)
                html_answer = str(soup)
                html = html_answer.format(title=title, text=text)

            htmls.append(html)

    next_page = rsp.json().get('resp_data').get('topics')
    if next_page:
        create_time = next_page[-1].get('create_time')
        end_time = create_time[:20]+str(int(create_time[20:23])-1)+create_time[23:]
        end_time = quote(end_time)
        if len(end_time) == 33:
            end_time = end_time[:24] + '0' + end_time[24:]
        next_url = start_url + '&end_time=' + end_time
        print(next_url)
        get_data(next_url)

    return htmls

def make_pdf(htmls):
    html_files = []
    for index, html in enumerate(htmls):
        file = str(index) + ".html"
        html_files.append(file)
        with open(file, "w", encoding="utf-8") as f:
            f.write(html)

    options = {
        "user-style-sheet": "jinghua.css",
        "page-size": "Letter",
        "margin-top": "0.75in",
        "margin-right": "0.75in",
        "margin-bottom": "0.75in",
        "margin-left": "0.75in",
        "encoding": "UTF-8",
        "custom-header": [("Accept-Encoding", "gzip")],
        "cookie": [
            ("cookie-name1", "cookie-value1"), ("cookie-name2", "cookie-value2")
        ],
        "outline-depth": 10,
    }
    try:
        pdfkit.from_file(html_files, "电子书.pdf", options=options)
    except Exception as e:
        print(e)

    for file in html_files:
        os.remove(file)

    print("已制作电子书在当前目录！")
    
if __name__ == '__main__':
    start_url = 'https://api.zsxq.com/v1.10/groups/8424258282/topics?scope=digests&count=20'
    make_pdf(get_data(start_url))