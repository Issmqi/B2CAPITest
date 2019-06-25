'''
__author__:'shimengqi'
__description__:'获取依赖接口返回数据'
__mtime_:2018/1/21
'''

import json
import ast
from readExcel import ReadExcel
from readConfig import ReadConfig
from log import Log
from TestXlsxReport import Report
from getDependValue import GetDependValue
import httpMethod

ReadConfig=ReadConfig()
log=Log()
ReadExcel=ReadExcel()
report=Report()
passcase=0

class BuyerTestCase:

    def __init__(self,rownum=None):
        self.caseId = int(ReadExcel.get_cell(rownum, 0))
        self.caseName = ReadExcel.get_cell(rownum, 2)
        self.APIName = ReadExcel.get_cell(rownum, 3)
        self.url = ReadExcel.get_cell(rownum, 4)
        self.method = ReadExcel.get_cell(rownum, 5)
        self.data = ReadExcel.get_cell(rownum, 6)
        self.expectCode=int(ReadExcel.get_cell(rownum,7))
        self.user=ReadExcel.get_cell(rownum,8)
        self.withParam=ReadExcel.get_cell(rownum,10)
        self.dependRow = ReadExcel.get_cell(rownum, 11)
        self.dependField = ReadExcel.get_cell(rownum, 12)
    def test_buyerCase(self,worksheet,temp):
        global passcase
        data=self.data
        # 判断接口是否依赖其他接口数据
        if self.dependRow != '':
            dependRow = int(self.dependRow)
            depend = GetDependValue(dependRow)
            dependValue = depend.getDependValue(self.dependField)
        data_dict=eval(data)
        data_json=json.dumps(data)
        log.debug('使用%s方法执行用例%s'%(self.method,self.caseName))
        if self.user=='Buyer':
            try:
                actual = httpMethod.buyerRequest(self.method, self.url, data_dict)
                # actual = httpMethod.buyerRequest(self.method, self.url, data_dict)
            except Exception:
                log.error("参数异常！")
            finally:
                report.write_basic(self.caseId,self.caseName,self.APIName,self.url,self.method,data,self.expectCode,worksheet,temp)
                log.info("基本数据写入成功")
            report.write_special(actual, self.expectCode, worksheet, temp)
            log.info("特殊数据写入成功")

        elif self.user=='Shop':
            try:
                actual=httpMethod.shopRequest(self.method,self.url,data_dict)
            except Exception:
                log.error("参数异常！")
            finally:
                report.write_basic(self.caseId,self.caseName,self.APIName,self.url,self.method,data,self.expectCode,worksheet,temp)
                log.info("基本数据写入成功")
            report.write_special(actual,self.expectCode,worksheet,temp)
            log.info("特殊数据写入成功")


        elif self.user=='Guest':
            try:
                actual=httpMethod.guestRequest(self.method,self.url,data_dict)
            except Exception:
                log.error("参数异常！")
            finally:
                report.write_basic(self.caseId,self.caseName,self.APIName,self.url,self.method,data,self.expectCode,worksheet,temp)
                log.info("基本数据写入成功")
            report.write_special(actual, self.expectCode, worksheet, temp)
            log.info("特殊数据写入成功")
        else:
            log.error("用户权限不存在！")


        resCode=actual['code']
        if resCode==self.expectCode:
            passcase += 1
            log.info('测试用例ID：%s' % self.caseId)
            log.info('测试API：%s' % self.APIName)
            log.info('测试用例名称：%s' % self.caseName)
            log.debug('测试通过')
            log.debug('测试返回数据：%s' % actual)
        else:
            log.info('测试用例ID：%s' % self.caseId)
            log.info('测试API：%s' % self.APIName)
            log.info('测试用例名称：%s' % self.caseName)
            log.debug('测试失败')
            log.debug('测试返回数据：%s' % actual)
        report.close_workbook()




def main():
    report.test_detail()
    report.init()
    sheet2=report.get_worksheet2()
    Buyer=BuyerTestCase(3)
    Buyer.test_buyerCase(sheet2, 3)
if __name__ == '__main__':
    main()






