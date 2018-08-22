#encoding=utf-8
import requests, json, sys
from twilio.rest import Client

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
        send_wechat(data['Message'])
    else:
        print("签到成功，获取到 {} 个积分".format(data['Data']['GetPoints']))
        send_wechat("签到成功，获取到 {} 个积分".format(data['Data']['GetPoints']))

def send_wechat1(text):
    url = "https://sc.ftqq.com/xxxx.send?text={}&desp={}".format('食行生鲜签到提醒',text)
    resp = requests.get(url)
    print(resp.status_code)

def send_wechat(text):
    url = "https://pushbear.ftqq.com/sub?sendkey=5250-xxxx&text={}&desp={}".format('食行生鲜签到提醒',text)
    resp = requests.get(url)
    print(resp.text)

def send_sms(text):
    account_sid = 'your_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                from_='your_from_num',
                                body=text,
                                to='your_to_num'
                            )
    print(message.sid)

if __name__ == "__main__":
    Phone = input('请输入账号：')
    PassWord = input('请输入密码：')

    customerguid, accesstoken = login(Phone.strip(), PassWord.strip())
    signin(customerguid, accesstoken)
