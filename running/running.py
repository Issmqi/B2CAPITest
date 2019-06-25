#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'shimengqi'
__description__:'运行测试框架'
__mtime__:2018/3/8
'''
from log import Log
from TestAllRunner import TestAllRunner
import time
from TestXlsxReport import Report
import TestSuite
import BuyerTestCase
from sendEmail import SendEmail

log=Log()
report=Report()
sendEmail=SendEmail()


class Running:
    def __init__(self):
        self.sheet=report.get_worksheet()
    def write_data(self,runcase,passcase,failcase,passrate,time):
        report.write_cell(self.sheet,"E3",runcase)
        report.write_cell(self.sheet, "E4", passcase)
        report.write_cell(self.sheet, "E5", failcase)
        report.write_area(self.sheet, "F4:F6", time, 's')
        report.write_area(self.sheet, "G4:G6", passrate, '%')

    def running(self):
        '''运行测试框架'''
        log.info("开始测试")
        start=time.time()
        start_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(start))
        log.info("当前时间是%s"%start_time)
        '''生成测试报告模版'''
        report.init()
        report.test_detail()

        '''执行测试用例'''
        sheet2=report.get_worksheet2()
        TestAllRunner().threads(sheet2)
        end=time.time()
        end_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(end))
        log.info("当前时间是%s"%end_time)
        '''获取用例数据并写入'''
        runcase=TestSuite.runcase-4
        passcase=BuyerTestCase.passcase
        failcase=runcase-passcase
        passrate=(passcase/runcase)*100
        self.write_data(runcase, passcase, failcase, passrate, end - start)
        report.close_workbook()
        report_address=report.get_workaddress()
        sendEmail.sendEmail(report_address)

        log.info('耗时：%s' % (end - start))
        log.info('测试完毕')

def main():
    Running().running()
if __name__ == '__main__':
    main()














