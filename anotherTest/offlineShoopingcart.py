import json
import requests

from business import buyerLogin
# 执行订单确认

host=buyerLogin.host
# host='http://www.raincard.cn'

def offlineShoppingcart():
    url = '/api/v1/buyer/shopping_cart/offline/create'

    params = {
        'sku_data':'[{"sku_id": "S007M9O0YO", "buy_vol": 1, "is_selected": 1}]'
    }

    re = requests.post(host + url, data=params)
    result = re.json()
    print(re.url)
    print('param:', params)
    print('response:', result)
    # return order_money
def onlineShopingCart():
    url = '/api/v1/buyer/shopping_cart/create'

    params = {
        'sku_json':'[{"sku_id": "S007M9O0YO", "buy_vol": 1}]'
    }

    re = buyerLogin.session.post(host + url, data=params)
    result = re.json()
    print(re.url)
    print('param:', params)
    print('response:', result)


def delShoppingCart():
    url = '/api/v1/buyer/shopping_cart/clear/create'



    re = buyerLogin.session.post(host + url)
    result = re.json()
    print(re.url)
    print('response:', result)

# offlineShoppingcart()
# onlineShopingCart()
delShoppingCart()