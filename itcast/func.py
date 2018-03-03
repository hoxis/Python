# coding=utf-8

def print_line(num):
    print('-' * num)

def sum(a,b,c):
    return a+b+c

a = 1

def test():
    global a
    print(a)
    a += 1

test()
print(a)

li = [1,2]

def test_list():
    li.append(3)
    print(li)

test_list()
print(li)

# print(sum(2,3,4))

print_line(10)

#########################
# 缺省参数
def printInfo(name, age=5):
    print('name is %s, age is %s' %(name, age))

printInfo('liuha', 20)
printInfo('liu2')
# printInfo()
##########################
print('-' * 10)
##########################
# 可变长参数
def func_test(a, b=2, *args, **kwargs):
    print('a = %s' %a)
    print('b = %s' %b)
    print('args = ' , args)
    print('kwargs = ' , kwargs)

func_test(1,2,3,4,k1=2,k2=3)
print('-'*5)

func_test(1,2,3,k1=2,k2=3)
print('-'*5)

func_test(1,k1=3)

##########################
# 引用传参
def add(a,b=33):
    a *= 2
    b = b * 2

a = 1
b = 1
add(a,b)
print('a = ', a)
print('b = ', b)
a_list = [2,3]
b_list = [2,3]
add(a_list, b_list)
print('a_list = ', a_list)
print('b_list = ', b_list)