import requests,json,time,uuid,os,openpyxl
import re
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

info_list = []

def get_comment_info():
    global info_list
    pagenum = 1
    while(True):
        print(pagenum)
        url = "https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg"

        querystring = {"biztype":"1","topid":"237773700","cmd":"8","pagenum":pagenum,"pagesize":"25"}

        response = requests.request("GET", url, params=querystring)

        resp = json.loads(response.text)

        commentlist = resp.get('comment').get('commentlist')

        if not commentlist or len(commentlist) == 0:
            return

        for comment in commentlist:
            info = []
            one_name = comment.get('nick')
            # 将 UNIX 时间戳转化为普通时间格式
            if comment.get('time') < 1568735760:
                return
            time_local = time.localtime(comment.get('time'))
            one_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
            one_praisenum = comment.get('praisenum')
            one_comment = comment.get('rootcommentcontent')
            ILLEGAL_CHARACTERS_RE.sub(r'', one_comment)
            ILLEGAL_CHARACTERS_RE.sub(r'', one_name)
            info = [one_name, one_time, one_praisenum, one_comment]
            # print(info)
            info_list.append(info)
        pagenum += 1
            # print(comment.get('nick'))
            # print(comment.get('rootcommentcontent'))
            # print(comment.get('time'))
            # print(comment.get('praisenum'))


def file_do(file_name):
    # 获取文件大小
    if not os.path.exists(file_name):
        wb = openpyxl.Workbook()
        page = wb.active
        page.title = 'jay'
        page.append(['昵称','时间','点赞数','评论'])
    else:
        wb = openpyxl.load_workbook(file_name)
        page = wb.active
    for info in info_list:
        try:
            page.append(info)
        except Exception:
            print(info)
            pass
        continue
    wb.save(filename=file_name)

if __name__ == "__main__":
    file_name = str(uuid.uuid1()) + '.xlsx'
    get_comment_info()
    file_do(file_name)
    print('data has saved in {}'.format(file_name))
