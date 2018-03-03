# coding=utf-8
'''
判断用户输入的年份是否是闰年的程序
'''

def func(year):
    year = int(year)
    if year < 0:
        print('请输入正确的年份')
        exit()
    
    if year % 400 == 0:
        return True
    else:
        if year % 4 == 0 and year % 100 != 0:
            return True

year = input('请输入正确的年份：')

if(func(year)):
    print('%s 是闰年' %year)
else:
    print('%s 不是闰年' %year)