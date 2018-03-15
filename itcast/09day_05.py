# coding=utf-8

# 继承
class Animal:
    def run(self):
        print('animal is running')

class Cat:
    def __init__(self, name, color='white'):
        self.name = name
        self.color = color

    def run(self):
        print('%s -- 在跑' %self.name)

class Bosi(Animal,Cat):
    def eat(self):
        print('%s -- 在吃饭' %self.name)


xiaomi = Cat('xiami')
xiaomi.run()

huihui = Bosi('huihui', 'hui')
huihui.eat()
huihui.run()

print(Bosi.__mro__)