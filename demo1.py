# coding = utf-8
from urllib.parse import urlencode

import requests
session = requests.Session()
# 1.获取cookie
start_url = "https://kyfw.12306.cn/otn/login/init"
session.get(start_url)
answer = ''
def get_cap():
    # 2.获取验证码
    captcha_url = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.11248564942476502"
    response = session.get(captcha_url)
    # print(response.content)
    with open('captcha.png', 'wb') as fp:
        fp.write(response.content)
# 3.校验验证码
def check():
    global answer
    answer= str(input())
    check_captcha_url = "https://kyfw.12306.cn/passport/captcha/captcha-check"
    data = {
        "answer": answer,
        "login_site": "E",
        "rand": "sjrand"
    }
    response = session.post(check_captcha_url, data=data)
    print(response.text)
# 4.校验用户名和密码
def login(answer):
    login_url = "https://kyfw.12306.cn/passport/web/login"
    data = {
        "username": '15165363708',
        "password": '19890513a',
        "appid": "otn",

    }
    response = session.post(login_url, data=data)
    print(response.request.url)
    print(response.text)

get_cap()
check()
login(answer)
