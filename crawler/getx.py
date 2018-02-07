# coding=utf-8

import bs4, requests

url = 'http://58.210.143.5:8001/Home/RegBrowse?examid=00180111113752'

while True:
    response = requests.get(url)
    print(response.status_code)

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    # text = soup.text.replace(u'\xa0', u' ')
    # print(text)
    # tables = soup.findAll('table')
    # print(tables)
    # tab = tables[0]
    data_list = [] 

    for idx, tr in enumerate(soup.find_all('tr')):
        print(tr.encode('gb2312'))
        if idx != 0:
            tds = tr.find_all('td')
            data_list.append({
                '部门名称': tds[0].contents[0],
                '职位名称': tds[1].contents[0],
                '开考比例': tds[2].contents[0],
                '招考人数': tds[3].contents[0],
                '报名人数': tds[4].contents[0]
            })
        # for th in tr.find_all('th'):
        #     print(th.encode('gb2312'))
        #     if '3050700030' in th:
        #         print(th.text.encode('gb2312'))
        print(data_list)