# coding=utf-8

# 多态
class F1(object):
    def show(self):
        print('F1.show')

class S1(F1):
    def show(self):
        print('S1.show')

class S2(F1):
    def show(self):
        print('S2.show')

def func(obj):
    obj.show()

if __name__ == '__main__':  
    s1 = S1()
    s2 = S2()

    func(s1)
    func(s2)