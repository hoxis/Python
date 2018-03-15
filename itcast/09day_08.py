# coding=utf-8

class People:
    # 设置为私有属性
    __address = '江苏'

    # 类方法，用 classmethod 来进行修饰
    @classmethod
    def getAddress(cls):
        return cls.__address

    @classmethod
    def setAddress(cls, address):
        cls.__address = address

# print(People.__address)
print(People.getAddress()) # 可以通过类对象引用

p = People()
print(p.getAddress()) # 可以用过实例对象引用

p.setAddress('湖南')
print(p.getAddress())
print(People.getAddress())

class People2:
    __country = 'China'

    @staticmethod
    def getCountry():
        return People2.__country

print(People2.getCountry())

p2 = People2()
print(p2.getCountry())