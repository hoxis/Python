# coding=utf-8

# 创建单例-保证只有1个对象
# 实例化一个单例
class Singleton(object):
    # 使用局部变量
    __instance = None

    def __new__(cls):
        # 如果 __instance 没有创建
        # 那么就创建一个对象，并且赋值为这个对象的引用
        # 保证下次调用这个方法时，能够知道之前已经创建过对象，这样就保证了只有一个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

a = Singleton()
b = Singleton()

print(id(a))
print(id(b))

a.age = 20

print(a.age)
print(b.age)

# 创建单例时，只执行1次__init__方法
class Singleton2(object):
    __instance = None
    __first_init = False

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self, age, name):
        if not self.__first_init:
            self.age = age
            self.name = name
            Singleton2.__first_init = True


a = Singleton2(18, "dongGe")
b = Singleton2(8, "dongGe")

print(id(a))
print(id(b))


print(a.age)
print(b.age)

a.age = 19
print(b.age)            