import json
import requests

# from business import buyerLogin
from readConfig import ReadConfig
from getToken import GetToken
# 执行订单确认
ReadConfig = ReadConfig()

host=ReadConfig.get_config("HTTP","host")
token=GetToken().getBuyertoken()
# host='http://www.raincard.cn'
def confirmOrder():

    url = '/api/v1/order/confirm/create'
    cookies = {"buyer_token": token}
    params = {
        'sku_json': '[{"sku_id":"S007M9O0YO","buy_vol":1,"price":1,"money_unit":"CNY"}]',
        'shop_id':126,
        "use_coupon_code":"-1",
        "address_id":75
    }

    re = requests.post(host + url, data=params,cookies=cookies)
    print('url=', re.url)
    print('params=', str(params))
    print(re.json())



    v = json.loads(re.text)
    # pay_amount = v['data']['pay_amount']
    # print('pay_amount：', pay_amount)



def createOrder():
    url = '/api/v1/order/create/create'

    params = {
        'sku_json': '[{"sku_id":"S007M9O0YO","buy_vol":1,"price":1,"money_unit":"CNY"}]',
        'shipping_address_json': '{"name":"师孟奇","province":"上海市","city":"上海市","district":"浦东新区","street":"上海市浦东新区博霞路22号","mobile":"13127908386","city_no":73}',
        'pay_amount': 1,
        'shop_id':'126',
        'use_coupon_code':-1,
        'id_card':'370402199009106047',
        'order_remark': '单个商品'
    }

    re = requests.post(host + url, data=params)
    result = re.json()
    print(re.url)
    print('param:', params)
    print('response:', result)
    # return order_money
confirmOrder()
# createOrder()