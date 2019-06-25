# encoding : utf-8       #设置编码方式
import json

import xlrd  # 导入xlrd模块
import xlwt
import httpMethod

# 打开指定文件路径的excel文件

xlsfile = r'D:/macys/TestCase/MacysTrack2.0 Sprint3_APITestCase.xlsx'
book = xlrd.open_workbook(xlsfile)  # 获得excel的book读对象
bookwrite=xlwt.Workbook(xlsfile)
sheet = book.sheet_by_index(1)  # 通过sheet索引获得sheet对象
sheetwrite=book.sheet_by_index(1)
nrows = sheet.nrows  # 行总数
# print('行总数是:'+str(nrows))
ncols = sheet.ncols  # 列总数
# print('列总数是:'+str(ncols))
# 获得指定行、列的值，返回对象为一个值列表

for i in range(3,nrows):
    caseName=sheet.cell_value(i,2)
    url = str(sheet.cell_value(i , 4))
    method = str(sheet.cell_value(i , 5))
    param_str=str(sheet.cell_value(i, 6))
    params = dict(eval(param_str))
    param=json.dumps(param_str)

    # params=exec(param_str)
    # print('第' + str(i) + '行caseName是：' + str(caseName))
    # print('第'+ str(i) +'行url是：'+url)
    # print('第' + str(i) + '行method是：' + method)
    # print('第' + str(i) + '行params是：' , params)

    httpMethod.buyerRequest(method,url,params)
    # print('执行结果是',result.json())








