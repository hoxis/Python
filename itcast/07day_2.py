# coding=utf-8
'''
求100-200里面所有的素数
素数的特征是除了1和其本身能被整除，其它数都不能被整除的数
'''

def func(start, end):
    start = int(start)
    end = int(end)
    a = start
    result = []
    if start == 1:
        start += 1
    for i in range(start, end+1):
        for j in range(2, i):
            # 获取所有非素数
            if i % j == 0:
                result.append(i)
                break
    # 反向获取素数
    result2 = [i for i in range(a,end+1) if i not in result]
    return result2

start = input('请输入起始数：')
end = input('请输入截止数：')
print('素数集合：', func(start, end))