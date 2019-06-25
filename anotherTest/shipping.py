import requests
import json
import shopLogin
host=shopLogin.host
def queryRecognise():
    url='/v1/thirdpart/logis/kuaidi100/recognise/query'
    param={'logistics_code':'813963246938'}
    param_str=json.dumps(param)
    re=shopLogin.session.get(host+url,data=param)
    print(re.url)
    print(param)
    print(re.text)

def getRecognise():
    url = '/v1/thirdpart/logis/kuaidi100/recognise/query'
    param = {
        'logistics_code': '813963246938',
        'token':'admin_token_7kBlV1cTjjKYDiyuw7xykCscmJPnvwjP'
    }
    param_str = json.dumps(param)
    re = requests.get(host + url, data=param)
    print(re.url)
    print(param)
    print(re.text)


# queryRecognise()

getRecognise()

