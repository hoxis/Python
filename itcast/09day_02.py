# coding=utf-8

'''
类与对象
'''

# 定义类
class SweetPotato():

    # 初始化函数，用来完成一些默认的设定
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = '生的'
        self.condiments = []

    def cook(self, time):
        self.cookedLevel += time
        if self.cookedLevel > 8:
            self.cookedString = '烤焦了的'
        elif self.cookedLevel > 5:
            self.cookedString = '熟了的'
        elif self.cookedLevel > 3:
            self.cookedString = '还有点生的'
        else:
            self.cookedString = '生的'

    def addCondiment(self, condiment):
        self.condiments.append(condiment)
    
    def __str__(self):
        msg = '烤了' + str(self.cookedLevel) + '分钟了，' + self.cookedString + '地瓜，有这些佐料：' + str(self.condiments)
        # if len(self.condiments) > 0:
        #     pass
        return msg

patato = SweetPotato()
print(patato)

patato.cook(2)
print(patato)

patato.addCondiment(u'番茄酱')

patato.cook(2)
print(patato)

patato.cook(2)
print(patato)

patato.addCondiment(u'沙拉酱')

patato.cook(2)
print(patato)

patato.cook(2)
print(patato)

patato.cook(2)
print(patato)