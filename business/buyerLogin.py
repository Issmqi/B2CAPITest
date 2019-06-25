import requests
import hashlib
import json
from util import readConfig
from log import Log
ReadConfig=readConfig.ReadConfig()
log=Log()

host=ReadConfig.get_config("HTTP","host")
mobile=ReadConfig.get_config("DATABASE","mobile")
buyer_id=ReadConfig.get_config("DATABASE","buyer_id")
shop_id=ReadConfig.get_config("DATABASE","shop_id")

session=requests.Session()

def buyerLogin():
    # host='http://www.raincard.cn'
    url='/api/v1/buyer/auth/sign/create'
    sign_str = "buyer_id=" + buyer_id + "&shop_id=" + shop_id + "Kbg6OdLm36vVpdn0Pp4x5OVB6SDovUmh"
    # sign_str = "mobile=" + mobile + "&shop_id=" + shop_id + "&Kbg6OdLm36vVpdn0Pp4x5OVB6SDovUmh"
    sign = hashlib.md5(sign_str.encode('utf - 8')).hexdigest().upper()
    # print(sign)
    params={
        # "mobile":mobile,
        "buyer_id": buyer_id,
        "shop_id":shop_id,
        "sign":sign
    }
    re=session.post(host+url,params)
    print(re.url)
    print(json.dumps(params))
    print(re.json())



def getSign():
    url='/api/v1/buyer/auth/sign/update'
    param={
        # "mobile": mobile,
        "buyer_id": buyer_id,
        "shop_id": shop_id,
        "secret_key": "Kbg6OdLm36vVpdn0Pp4x5OVB6SDovUmh"
    }
    re=requests.post(host+url,param)
    result=re.json()
    sign=result['data']
    print(sign)
    return sign



buyerLogin()
