# coding=utf-8

__all__ = ["Test", "test1"]

class Test(object):
    def test(self):
        print('This is test.')

def test1():
        print('This is test1.')

def test2():
    print("This is test2.")

print(__name__)

# 测试函数
if __name__ == "__main__":
    t = Test()
    t.test()
    test1()
    test2()