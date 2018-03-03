# coding:utf-8

# print('''
#     ==================================
#     =        欢迎进入到身份认证系统V1.0
#     = 1. 登录
#     = 2. 退出
#     = 3. 认证
#     = 4. 修改密码
#     ==================================
# ''')

print('请输入姓名')

input_name = input()

name = 'liuhaha'

if name == input_name:
    print('亲爱的 %s ，欢迎登陆 爱学习管理系统' % name)
else:
    print('姓名不正确')