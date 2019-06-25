import json

print("hello world")
a={"name":"师孟奇"}
a_str=json.dumps(a)
b={'sku_data':'[{"sku_id":"S00GADYZRF","buy_vol": "1.5", "is_selected": 1}]'}
b_str=json.dumps(b)
a_dict=eval(a)
print("你好，世界!")
print(a)
print(a_dict)
print(b)