import json
import requests

from business import buyerLogin


host=buyerLogin.host
def getCard():
    url='/api/v1/buyer/id_card/query'
    param={
        "name":"师孟奇",
        "shop_id":"126"
    }
    param_str=json.dumps(param)
    re=buyerLogin.session.get(host+url,data=param)
    print("param:",param)
    print(re.json())
getCard()