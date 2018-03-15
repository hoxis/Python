# coding=utf-8

# 私有属性
class Person:
    def __init__(self, name='xiaoming'):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

class Person2(object):
    def __init__(self, name='xiahua'):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

xiaobi = Person()
print(xiaobi.getName())
print(xiaobi.name)
xiaobi.name = 'xiaoci'
print(xiaobi.name)
xiaobi.setName('xiaodi')
print(xiaobi.name)

dabi = Person2()
print(dabi.__name)