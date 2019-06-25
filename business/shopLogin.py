import json
import requests
from readConfig import ReadConfig
from log import Log

ReadConfig=ReadConfig()
log=Log()
session = requests.Session()
# host=ReadConfig.get_config("HTTP","host")
host='http://wesufu.top'
def userLogin():
    url = '/api/v1/user/auth/login/create'
    params = {
        'remember': '1',
        'username': 'fuwy@foxmail.com',
        'password': 123456
    }
    param_str = json.dumps(params)
    re = session.post(host + url, data=params)
    log.info("用户登录成功！")
    # print(re.json())
    # result = requests.get('https://m.test.wemartx.com/wm/api/v1/user/auth/login/create')


def shopLogin():
    # session = requests.session()
    url = '/api/v1/channel/shop/auth/login/create'
    params = {
        'shop_id': 7

    }
    param_str = json.dumps(params)
    re = session.post(host + url, data=params)
    log.info("商户登录成功！")
    # print(re.json())
userLogin()
shopLogin()

