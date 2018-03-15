# coding=utf-8

# 类属性
class People:
    name = 'Tom' # 公有的类属性
    __age = 12 # 私有类属性

p = People()

print(p.name)            # 正确
print(People.name)      # 正确
# print(p.__age)          #错误，不能在类外通过实例对象访问私有的类属性
# print(People.__age)     #错误，不能在类外通过类对象访问私有的类属性

print('-' * 20)


# 实例属性
class People2:
    address = '山东'
    def __init__(self):
        self.name = 'sb'
        self.age = 22

p2 = People2()
print(p2.age)
p2.age = 12
print(p2.age)
print(p2.name)
print(p2.address)

print(People2.address)
# print(People2.name) # 错误，不能获取到实例属性
# print(People2.age)

p2.address = '江苏' # 会新增一个实例属性，不会影响到类属性
print(p2.address) # 实例属性会屏蔽掉同名的类属性
print(People2.address) # 类属性没有变化

People2.address = '四川'
print(p2.address) # 仍然是 江苏
print(People2.address)

del p2.address
print(p2.address)

del p2.age
print(p2.age)