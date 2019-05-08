'''
提取验证码

'''
import requests
from PyQt5.Qt import *
import os
import json
# url 解码
from urllib.parse import unquote
import re
import time
import base64


class TimeTool(object):

    @staticmethod
    def format_train_time(train_time):
        date_str = time.strptime(train_time, "%Y%m%d")
        time_tamp = time.mktime(date_str)
        time_local = time.localtime(time_tamp)
        formats = "%a %b %d %Y %H:%M:%S GMT+0800 (China Standard Time)"
        return time.strftime(formats, time_local)



class Api_Login(QObject):

    YZM_URL= 'https://kyfw.12306.cn/passport/captcha/captcha-image'
    UA = {
        # "Connection": "keep-alive",
        # "Host": "kyfw.12306.cn",
        "Referer": "https://kyfw.12306.cn/otn/login/init",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
        # "X-Requested-With": "XMLHttpRequest"
    }
    # 座位席别
    seat_type = {
        "WZ":"无座",
        "F":"动卧",
        "M":"一等座",
        "O":"二等座",
        "1":"硬座",
        "3":"硬卧",
        "4":"软卧",
        "6":"高级软卧",
        "9":"商务座",
    }
    session = requests.session()
    check_yzm_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check' # 验证码校验url post
    check_login_url = 'https://kyfw.12306.cn/passport/web/login' # 登录校验 post
    set_cookie_tk_url = 'https://kyfw.12306.cn/passport/web/auth/uamtk' # 设置tk cookie post
    set_cookie_client_url = 'https://kyfw.12306.cn/otn/uamauthclient' # 设置cli coolie post
    user_base_info_url = 'https://kyfw.12306.cn/otn/index/initMy12306Api' # 获取登录欢迎信息 post
    # 车站列表 get
    station_name_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9100'

    # 查票url get
    '''
    leftTicketDTO.train_date: 2019-05-07 出发日期
    leftTicketDTO.from_station: SHH 出发站
    leftTicketDTO.to_station: TJP 到大站
    purpose_codes: ADULT 成人票
    '''
    query_tickets_url = 'https://kyfw.12306.cn/otn/leftTicket/query'

    # 订票之前验证用户是否登录 post data = {"_json_att": ""}
    checkUser_url = 'https://kyfw.12306.cn/otn/login/checkUser'

    # 提交订单请求 post
    data = '''
    secretStr: lakPkottZNn4YnrwCWjhkBrOm0YdWVaNlHn2FXBYx97qBPAh7jWBKxtt7U3nDYSVe8fKLXqZStXy
    +XCSVgaOLvLj7CUH0gYpgsWiFjZ/XfB3EzsN6acInID1fB4gFjApunkLahaa2s6Uw5m1w2yVxuuT
    70LYZl/aLcOMjkI0FlgLvx7NFwl4rHRaCrY8idILcuAo1btrZWnqRZoSWAQxoDwobnb8oS6vIQGp
    +4QLV9BT78deCkikY66oyM2h5JEY4c5lVv+sP43xgJIYvAheYDy3gdlGP3RQps0XE6uT2lUamtaK
    MxveHQ==
    train_date: 2019-05-08
    back_train_date: 2019-05-07
    tour_flag: dc
    purpose_codes: ADULT
    query_from_station_name: 北京
    query_to_station_name: 天津
    undefined: 
    '''
    submitOrderRequest_url = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'

    # 获取登录token post data = {"_json_att": ""}
    submit_token_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'

    # 获取联系人信息url post data = {_json_att:
    # REPEAT_SUBMIT_TOKEN: 2816485ab7981a37cc0f10b175c58da7}
    getPassengerDTOs_url = 'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'

    # 检查订单信息 post
    checkOrderInfo_url = 'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo'

    # 订单队列 post
    getQueueCount_url = 'https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount'

    # 下订单 post
    confirmSingleForQueue_url = 'https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue'


    # 获取验证码
    @classmethod
    def get_yzm(cls):
        response = cls.session.get(cls.YZM_URL, headers=cls.UA)
        # 获取验证码的绝对路径
        path = os.path.split(os.path.realpath(__file__))[0] + '/captcha.jpg'

        with open(path, 'wb') as f:
            f.write(response.content)

        return 'api/captcha.jpg'

    # 校验验证码
    @classmethod
    def check_yzm(cls, point):
        data = {
                "answer": point,
                "login_site": "E",
                "rand": "sjrand"

        }
        response = cls.session.post(cls.check_yzm_url, data=data)
        print(response.text)
        return response.json()['result_code']

    # 登录校验
    @classmethod
    def check_login(cls, username, pwd, points):
        # cls.session.get('https://www.12306.cn/index/script/core/lib/handlebars.js')
        # print(cls.session.cookies)
        # UA = {
        #     "Accept":"application/json, text/javascript, */*; q=0.0",
        #     "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        #     "Origin":"https://kyfw.12306.cn",
        #     "Referer":"https://kyfw.12306.cn/otn/login/init",
        #     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
        #     "X-Requested-With": "XMLHttpRequest"
        # }
        data = {

            "username": username,
            "password": pwd,
            "appid": "otn",
            "answer": points
        }
        # response = cls.session.post(cls.check_login_url, data=data, headers=UA, allow_redirects=False)
        # 经过试验需要添加如下cookie，不然请求会重定向到error.html
        cls.session.cookies.update({

            # 'RAIL_EXPIRATION': '1557374105201',
            'RAIL_DEVICEID': 'Q6HceYNHWmSaLAt4lsdvWKK6KdxAU33Ag3mrjyouiL4MzAii_urTlbvJhBXc2ImnutLliR5UBhVnNnjvrXIkZYc6BuBY4vDQTBIXWAkiV21UOU1OeTsf8OZYXSkrUMjD_PkK2PkWwZE4QxyF3TQq-K4f6kBeM4Q8',
            # 'route': '6f50b51faa11b987e576cdb301e545c4',

        })
        response = cls.session.post(cls.check_login_url, data=data)
        # with open('1.html', 'wb') as f:
        #     f.write(response.content)
        # print(response.history)
        # print(response.request.url)
        print(response.text)
        # print("session.cookie1:", cls.session.cookies)

    # 设置tk cookie 授权客户端
    @classmethod
    def author_cli(cls):
        response = cls.session.post(cls.set_cookie_tk_url, data={"appid": "otn"})
        print(response.json())
        tk = response.json()['newapptk']
        response2 = cls.session.post(cls.set_cookie_client_url, data={"tk":tk})
        # print(response2.text)
        # print("session.cookie2:", cls.session.cookies)
        return response2.json()['result_code']

    # 获取欢迎信息
    @classmethod
    def get_user_base_info(cls):
        response = cls.session.post(cls.user_base_info_url)
        print(response.text)

    # 获取车站信息
    @classmethod
    def get_station_name(cls):
        """
        # 把车站和对应的编码缓存到本地文件
        如果文件不存在则生成文件
        :return:
        """
        # 获取文件的绝对路径
        path = os.path.split(os.path.realpath(__file__))[0] + '/stations.json'
        path_re = os.path.split(os.path.realpath(__file__))[0] + '/re_stations.json'
        if os.path.exists(path):
            print('文件已存在')
        else:
            resp = requests.get(cls.station_name_url)
            city_names = resp.text.split('@')
            city_dic = {}
            re_city_dic = {}
            for city_name in city_names:
                items = city_name.split('|')
                if len(items) == 6:
                    # print(items)
                    city_dic[items[1]] = items[2]
                    re_city_dic[items[2]] = items[1]
            # print(city_dic, type(city_dic))
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(city_dic, f)
            with open(path_re, 'w', encoding='utf-8') as f:
                json.dump(re_city_dic, f)

    # 车次查询
    @classmethod
    def query_tickets(cls, seat_type=None):
        '''

        :param seat_type: 选择座位席别
        :return:
        '''
        params = {
            'leftTicketDTO.train_date': '2019-05-08',
            'leftTicketDTO.from_station': 'BJP',
            'leftTicketDTO.to_station': 'TJP',
            'purpose_codes': 'ADULT',
        }
        resp = requests.get(cls.query_tickets_url, params=params)
        # print(resp.text)
        train_info_list = []
        for data in resp.json()['data']['result']:
            train_info = {}
            train_info['密文'] = data.split('|')[0]
            train_info['车次'] = data.split('|')[3]
            train_info['车辆编号'] = data.split('|')[2]
            train_info['出发日期'] = data.split('|')[13]
            train_info['车辆位置'] = data.split('|')[15]
            train_info['余票'] = data.split('|')[12]
            train_info['始发站'] = data.split('|')[4]
            train_info['终点站'] = data.split('|')[5]
            train_info['上车站'] = data.split('|')[6]
            train_info['下车站'] = data.split('|')[7]
            train_info['出发时间'] = data.split('|')[8]
            train_info['到达时间'] = data.split('|')[9]
            train_info['历时'] = data.split('|')[10]
            train_info['商务座'] = data.split('|')[32]
            train_info['一等座'] = data.split('|')[31]
            train_info['二等座'] = data.split('|')[30]
            train_info['高级软卧'] = data.split('|')[21]
            train_info['软卧'] = data.split('|')[23]
            train_info['硬卧'] = data.split('|')[28]
            train_info['无座'] = data.split('|')[26]
            train_info['硬座'] = data.split('|')[29]
            train_info['是否可预订'] = data.split('|')[11]
            if not seat_type:
                # print(train_info)
                train_info_list.append(train_info)
            else:
                type = cls.seat_type[seat_type]
                if train_info[type] == '有' or train_info[type].isdigit():
                    # print(train_info)
                    train_info_list.append(train_info)
        # print(train_info_list)
        return train_info_list
            # if data.split('|')[3] == '2601':
            #     for idx, d in enumerate(data.split('|')):
            #         print(idx, d)
                # print(data)

    # 订票之前再一次验证用户登录信息
    @classmethod
    def check_user(cls):
        try:
            resp = cls.session.post(cls.checkUser_url, data={"_json_att":''})
            print("-"*50)
            print(resp.json()['data']['flag'])
            return resp.json()['data']['flag']
        except:
            return False

    # 获取登录token
    @classmethod
    def get_token(cls):
        resp = cls.session.post(cls.submit_token_url, data = {"_json_att": ""})
        # print(resp.text)
        token = re.findall(r"var globalRepeatSubmitToken = '(.*?)'", resp.text)
        key_changed = re.findall(r"'key_check_isChange':'(.*?)'", resp.text)
        print(token,key_changed[0])
        return token[0], key_changed[0]

    # 获取联系人信息
    @classmethod
    def getPassenger_info(cls, token):

        data = {
            "_json_att":"",
            "REPEAT_SUBMIT_TOKEN":token,
        }
        res = cls.session.post(cls.getPassengerDTOs_url, data=data)
        # print(res.text)
        return res.json()['data']['normal_passengers']

    # 订票
    @classmethod
    def book_ticket(cls, train_info):
        print('---------------------------订票--------------------------')
        print(train_info)
        # 订票之前再一次验证用户登录信息
        path_re = os.path.split(os.path.realpath(__file__))[0] + '/re_stations.json'
        with open(path_re, 'r') as load_f:
            load_dict = json.load(load_f)
        from_station_name = load_dict[train_info['上车站']]
        to_station_name = load_dict[train_info['下车站']]
        data = {
            'secretStr': unquote(train_info['密文'], 'utf-8'),
            'train_date': '2019 - 05 - 08',
            'back_train_date': '2019 - 05 - 07',
            'tour_flag': 'dc',
            'purpose_codes': 'ADULT',
            'query_from_station_name': from_station_name,
            'query_to_station_name': to_station_name,
            'undefined': ""
        }
        print(data)
        try:
            resp = cls.session.post(cls.submitOrderRequest_url, data=data)
            print(resp.text)
            return resp.json()['status']
        except:
            return False


    # 检查订单信息
    @classmethod
    def check_order_info(cls, token):
        print('---------------------------检查订单--------------------------')

        data = {

               'cancel_flag': 2,
               'bed_level_order_num': 000000000000000000000000000000,
               'passengerTicketStr': '3,0,1,刘殿君,1,372925199002043139,15165363708,N_3,0,1,刘琳琳,1,372925198810123124,18201476131,N',
                "oldPassengerStr": "刘殿君,1,372925199002043139,1_刘琳琳,1,372925198810123124,1_",
                'tour_flag': 'dc',
                'randCode':'',
                'whatsSelect': 1,
                '_json_att':'',
                'REPEAT_SUBMIT_TOKEN': token,
        }
        res = cls.session.post(cls.checkOrderInfo_url, data=data)
        print(res.text)


    # 获取订单队列
    @classmethod
    def get_queue_count(cls,train_info, token):
        print('---------------------订单队列-------------------------')

        data = {
            "train_date": TimeTool.format_train_time(train_info['出发日期']), # 日期 Wed May 08 2019 00:00:00 GMT+0800 (中国标准时间)
            "train_no": train_info['车辆编号'], # 列车编号
            "stationTrainCode": train_info['车次'], # 车次
            "seatType": 3, # 席别
            "fromStationTelecode": train_info['上车站'], #出发站
            "toStationTelecode": train_info['下车站'] ,# 到达站
            "leftTicket": train_info['余票'],# 剩余车票
            "purpose_codes": "00" ,
            "train_location": train_info['车辆位置'],
            "_json_att: ": "" ,
            "REPEAT_SUBMIT_TOKEN": token ,

        }
        print(data)
        res = cls.session.post(cls.getQueueCount_url, data=data)
        print(res.text)

    # 下订单
    @classmethod
    def confirmSingleForQueue(cls,token,key_check_isChange, train_info):
        data = {
            'passengerTicketStr': '3,0,1,刘殿君,1,372925199002043139,15165363708,N_3,0,1,刘琳琳,1,372925198810123124,18201476131,N',
            "oldPassengerStr": "刘殿君,1,372925199002043139,1_刘琳琳,1,372925198810123124,1_",
            "randCode": "",
            "purpose_codes": "00",
            "key_check_isChange":key_check_isChange,
            "leftTicketStr":train_info['余票'],
            "train_location": train_info['车辆位置'],
            "choose_seats": "",
            "seatDetailType": "000",
            "whatsSelect": 1,
            "roomType": 00,
            "dwAll": "N",
            "_json_att":"",
            "REPEAT_SUBMIT_TOKEN":token
        }
        res = cls.session.post(cls.confirmSingleForQueue_url, data=data)
        print(res.text)

if __name__ == '__main__':
    # Api_Login.get_yzm()
    train = Api_Login.query_tickets()
    # Api_Login.book_ticket(train[0])
    # Api_Login.get_station_name()
    # path = os.path.split(os.path.realpath(__file__))[0]
    # print(path)
    data  = '''
    QUw4KHGW1JKmnMjnO6WZtMoWyWOlGkvGaCCkWv0DyMGh2BWOLAT58cZ%2Bxe%2B5bfxSbvhAcc6CWM79%0Ary%2BxTfQla29xGKlgxPt56weT7OoGchJ4mEuvehi0DhYii05XlSix7HIQhbsQwInmMz9LkQW21yJ5%0AoxmZj%2BXt5FlydAS8Q9hFaXdY0hq9GSKUzwG4TvqRlxEwEG8quHppZJkv0pRWR2iIimYKRXFdrytU%0AwVq%2FwRRjhJY6JTPH%2FyIz1WNCQzRO3fij5yhhIWD4uV%2BrQW5tMYDgdCmW%2BUhVCwlgSv9vw%2ByB0dyl%0ANWZ4QA%3D%3D|预订|550000K51167|K511|SNH|VUQ|SNH|GZQ|19:21|17:08|21:47|Y|G2KTCvDnlNH%2FEZV1IUy5XdQjoXav4YQv7ft4vxMc0ZSizscpoOythHiTqRc%3D|20190507|3|H2|01|18|0|0||||7|||有||无|有|||||10403010|1431|0|0|null
    '''
    for idx, d in enumerate(data.split('|')):
        print(idx, d)
    # print(data)
    # print(TimeTool.format_train_time("20110101"))






