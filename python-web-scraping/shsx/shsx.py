#encoding=utf-8
import requests, json, sys


def login(Phone, PassWord):
    url = "https://wechatx.34580.com/sz/Sign/SignInV2"
    payload = {
        'SourceType': 9,
        'Phone': Phone,
        'PassWord': PassWord
    }

    # 测试下来发现，连 header 都不需要
    response = requests.post(url, data=json.dumps(payload))
    data = json.loads(response.text)
    is_error = data['Error']

    # 登录失败直接退出
    if is_error:
        print('登录失败：{}'.format(data['Message']))
        sys.exit(1)
    else:
        print('登录成功！')
        return data['Data']['CustomerGuid'], data['Data']['AccessToken']


def signin(customerguid, accesstoken):
    url = "https://wechatx.34580.com/sz/SignUp/CustomerSignUp"

    querystring = {"accesstoken": accesstoken,
                   "customerguid": customerguid, "sourcetype": "9"}

    # 这次不需要 body 中的传入数据
    response = requests.post(url, params=querystring)
    data = json.loads(response.text)
    is_error = data['Error']
    if is_error:
        print(data['Message'])
    else:
        print("签到成功，获取到 {} 个积分".format(data['Data']['GetPoints']))


if __name__ == "__main__":
    Phone = input('请输入账号：')
    PassWord = input('请输入密码：')

    customerguid, accesstoken = login(Phone.strip(), PassWord.strip())
    signin(customerguid, accesstoken)
