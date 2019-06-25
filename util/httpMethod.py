import json
import requests
import buyerLogin
import shopLogin
from readConfig import ReadConfig
from log import Log
from getToken import GetToken

ReadConfig=ReadConfig()
log=Log()
buyer_token=GetToken().getBuyertoken()

host = ReadConfig.get_config("HTTP","host")


def buyerRequest(method,url,params):
    cookies = {"buyer_token": buyer_token}
    # global host

    try:
        if method == "post":
            re = requests.post(host + url, data=params,cookies=cookies)
        if method == "get":
            re = requests.get(host + url, data=params,cookies=cookies)
        if method == "delete":
            re = requests.delete(host + url, data=params,cookies=cookies)
        result = re.json()
    except:
        print("请求类型不存在！")

    param_str=json.loads(json.dumps(params))
    # params_str=json.loads(params)
    print('url=', host + url)
    print('params=',params)
    print('response=',result)
    return result

# def buyerRequest(method,url,params):
#
#     # global host
#     if method == "POST":
#         re = buyerLogin.session.post(host + url, data=params)
#     elif method == "GET":
#         re = buyerLogin.session.get(host + url, data=params)
#     elif method == "DELETE":
#         re = buyerLogin.session.delete(host + url, data=params)
#     else:
#         log.error("请求类型不存在！")
#     result = re.json()
#
#     param_str=json.loads(json.dumps(params))
#     # params_str=json.loads(params)
#     print('url=', host + url)
#     print('params=',params)
#     print('response=',result)
#     return result



def shopRequest(caseName,method,url,params):
    print('----------',caseName,method,url,params)

    param_str = json.dumps(params)
    if method=="post":
        re = shopLogin.session.post(host + url, data=params)
        result = json.dumps(json.loads(re.text), ensure_ascii=False)

    if method == "get":
        re = shopLogin.session.get(host + url, data=params)
        result = re.json()
        # result = json.dumps(json.loads(re.text), ensure_ascii=False)
    if method == "delete":
        re = shopLogin.session.delete(host + url, data=params)
        result = json.dumps(json.loads(re.text), ensure_ascii=False)

    print('url=', host + url)
    print('params=', params)
    print( result)
    # return result

def guestRequest(method,url,params):

    # global host
    if method == "post":
        re = requests.post(host + url, data=params)
    elif method == "ge":
        re = requests.get(host + url, data=params)
    elif method == "delete":
        re = requests.delete(host + url, data=params)
    else:
        log.error("请求类型不存在！")
    result = re.json()

    param_str=json.dumps(params)
    print('url=', host + url)
    print('params=',params)
    print(result)
    return result




