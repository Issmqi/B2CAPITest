'''
__author__:'shimengqi'
__description__:'获取依赖接口返回数据'
__mtime_:2018/3/21
'''


import ast
from readExcel import ReadExcel
from readConfig import ReadConfig
from log import Log
from TestXlsxReport import Report
import httpMethod

ReadConfig=ReadConfig()
log=Log()
ReadExcel=ReadExcel()


class GetDependValue:
    def __init__(self,rownum=None):
        self.url = ReadExcel.get_cell(rownum, 4)
        self.method = ReadExcel.get_cell(rownum, 5)
        self.data = ReadExcel.get_cell(rownum, 6)
        self.user = ReadExcel.get_cell(rownum, 8)

    def getDependValue(self,dependField):
        global passcase
        data=self.data
        # log.debug("data的数据类型是%s"%type(data))
        data_dict=ast.literal_eval(data)
        # log.debug('使用%s方法执行用例%s'%(self.method,self.caseName))
        if self.user=='Buyer':
            try:
                result=httpMethod.buyerRequest(self.method,self.url,data_dict)
                # print(result)
            except Exception:
                log.error("参数异常！")

        elif self.user=='Shop':
            try:
                result=httpMethod.shopRequest(self.method,self.url,data_dict)
            except Exception:
                log.error("参数异常！")


        elif self.user=='Visitor':
            try:
                result=httpMethod.vistorRequest(self.method,self.url,data_dict)
            except Exception:
                log.error("参数异常！")
        else:
            log.error("用户权限不存在！")
        dependValue=result['data'][dependField]

        return dependValue
def main():

    dependCase=GetDependValue(39)
    v=dependCase.getDependValue('order_money')
    # dependValue=v['data']['order_money']
    print(v)

if __name__ == '__main__':
    main()




