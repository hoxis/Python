# 生成器
def f():
    print('start')
    a = yield 1  # 可以返回参数1，并接收传递的参数给a
    print(a)
    print('middle')
    b = yield 2  # 可以返回参数2，并接收传递的参数给b
    print(b)
    print('next')
    c = yield 3  # 可以返回参数3，并接收传递的参数给c
    print(c)  # 这里貌似永远不会执行，因为总会在上一行的yield处结束


a = f()  # 这里不会执行，即没有任何打印信息
# a.next() #这种写法在python3里面会报错
return1 = next(a)  # 输出start，中断在yield 1处，返回yield后面的1给return1
# return1 = a.send(None) # 效果同上一条语句
# return1 = a.send('test') # 这里会报错，生成器启动时只能传入 None，因为没有变量接收传入的值， TypeError: can't send non-None value to a just-started generator

# 如果首次执行generator，就传递一个非None的参数，因为第一次执行不是从一般的中断yield处执行起，所以没有yield关键字来接收传参，就会报错
print(return1)
return2 = next(a)  # 传入参数为None，即a=None，返回2给return2
print(return2)
return3 = a.send('msg')  # 传入参数msg，即b=msg,返回3给return3
print(return3)
