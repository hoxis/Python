# coding=utf-8

'''
类与对象
'''

# 定义类
class Car():

    # 初始化函数，用来完成一些默认的设定
    # def __init__(self):
    #     self.color = '蓝色'
    #     self.wheelNum = 2

    def __init__(self, wheelNum, color):
        self.color = color
        self.wheelNum = wheelNum

    def __str__(self):
        msg = "I'm a car. my color is " + self.color + ", and I hava " + str(self.wheelNum) + "个轮子."
        return msg
        

    # 移动
    def move(self):
        print('车在跑。。。')

    # 鸣笛
    def toot(self):
        print('车在叫。。。')

# 创建对象
# Bmw = Car();

# # 给对象添加属性
# # 如果后面再次出现BMW.color = xxx表示对属性进行修改
# # Bmw.color = '黑色'
# # Bmw.wheelNum = 4
# Bmw.move()
# Bmw.toot()

# print(Bmw.color)
# print(Bmw.wheelNum)

Qq = Car(4, '黄色')
print(Qq.color)
print(Qq.wheelNum)
print(Qq)