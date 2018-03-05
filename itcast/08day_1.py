# coding=utf-8
'''
制作一个"密码薄"
其可以存储一个网址（例如 www.itcast.cn），和一个密码(例如 123456)，
请编写程序完成这个“密码薄”的增删改查功能，
并且实现文件存储功能
'''

import os, re

print('1. 新增密码')
print('2. 修改密码')
print('3. 查询密码')
print('4. 删除密码')


num = input('请选择操作：')

if not re.match(r'[1-4]', num):
    print('请选择正确的操作')
    exit()

num = int(num)

f = None

# 新增密码
if num == 1:
    www = input('请输入网址：')
    # 判断网址是否已存在
    if os.path.isfile(www):
        print('%s 已存在' %www)
    else:
        passwd = input('请输入密码：')
        f = open(www, 'w+')
        f.write(passwd)
        print('保存成功')
# 修改密码
elif num == 2:
    www = input('请输入要修改的网址：')
    if os.path.isfile(www):
        passwd = input('请输入密码：')
        f = open(www, 'w+')
        f.write(passwd)
        print('保存成功')
    else:
        print('网址：%s 不存在' %www)
# 查询密码
elif num == 3:
    www = input('请输入网址：')
    if os.path.isfile(www):
        f = open(www, 'r')
        print('密码为：', f.readline())
    else:
        print('网址：%s 不存在' %www)
# 查询密码
# 删除密码  
else:  
    www = input('请输入待删除网址：')
    if os.path.isfile(www):
        os.remove(www)
        print('删除成功')
    else:
        print('网址：%s 不存在' %www)

if f != None:
    f.close()