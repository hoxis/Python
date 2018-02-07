import re
import sys
from sys import argv

if __name__ == '__main__':

    pwd = argv[1]
    print(pwd)
    # 检查字符长度是否小于8
    reg = re.compile(r'.{8,}')
    result = reg.search(pwd)
    if result == None:
        print("字符串长度必需大于8")
        sys.exit(1)

    # 检查是否包含大写字母
    reg = re.compile(r'[A-Z]+[a-z]+\d+')
    result = reg.search(pwd)
    if result == None:
        print("字符串需包含大写字母和小写字母")
        sys.exit(1)
    
    # 检查是否包含小写字母
    reg = re.compile(r'[a-z]+')
    result = reg.search(pwd)
    if result == None:
        print("字符串需包含大写字母")
        sys.exit(1)
    
    # 检查是否包含数字
