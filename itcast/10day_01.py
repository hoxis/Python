# coding=utf-8
import time
try:
    f = open('test.txst', 'r')
    try:
        while True:
            content = f.readline()
            if(len(content) == 0):
                break
            time.sleep(2)
            print(content)
    except:
        print('发生异常')
    finally:
        f.close()
        print('finally 关闭文件')
except Exception as e:
    print(e)
    print('没有这个文件')
finally:
    print("最后的finally")