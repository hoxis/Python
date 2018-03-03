# coding=utf-8
'''
实现 9*9乘法表
'''

for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s' %(j,i,i*j),  end=' ')
    print()
