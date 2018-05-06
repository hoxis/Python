# class Person(object):
#     def __init__(self, age = 18):
#         # 私有化属性，无法从外部直接获取
#         self.__age = age
    
#     def setAge(self, age):
#         self.__age = age
    
#     def getAge(self):
#         return self.__age

# p1 = Person()
# # print(p1.__age) # 会报错
# print(p1.getAge())
# print(dir(p1))

# # 相当于为 p1 新分配一个 __age 属性
# p1.__age = 20
# print(dir(p1))

# print(p1.__age)
# print(p1.getAge())

# name = "hoxis"
# _name = "hah"
# __name = "e"


class Money(object):
    def __init__(self):
        self.__money = 0

    @property
    def xmoney(self):
        return self.__money

    @xmoney.setter
    def xmoney(self, money):
        if isinstance(money, int):
            self.__money = money
        else:
            print("error: 不是整型数字")
    # money = property(getMoney, setMoney)

# m = Money()
# # print(m.getMoney())
# print(m.mmoney)
# m.mmoney = 20
# print(m.mmoney)
