class Person(object):
    def __init__(self, name):
        self.name = name

xiaoli = Person('小里')
print(xiaoli.name)

# 运行的过程中给对象绑定属性
xiaoli.age = 12
print(xiaoli.age)
# age 属性只属于 xiaoli，Person中并没有
print(dir(Person))
print(dir(xiaoli))

# 运行的过程中给类绑定属性
Person.address = None
print(dir(Person))

xiaoni = Person("小妮")
xiaoni.address = "江苏"
print(xiaoni.address)

# 运行的过程中给实例绑定方法
def run(self):
    print("%s is running" %self.name)

import types
# 不能直接使用 xiaoli.run = run
xiaoli.run = types.MethodType(run, xiaoli)
print(dir(Person))
print(dir(xiaoli))

xiaoli.run()

# 运行的过程中给类绑定方法
Person.run = run
print(dir(Person))
print(dir(xiaoli))
xiaoni.run()

# 运行中删除类的方法
delattr(Person, "run")
# del Person.run
del Person.address
print(dir(Person))