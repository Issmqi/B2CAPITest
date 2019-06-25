#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'shimengqi'
__description__:'运行所有开启的测试用例并选择对应方法'
__mtime__:2018/3/7
'''

import time
from readExcel import ReadExcel
from BuyerTestCase import BuyerTestCase
from log import Log
from TestXlsxReport import Report

ReadExcel = ReadExcel()
log = Log()
report=Report()
runcase = 2

class TestAllCase:
    def __init__(self):
        # 从excel提取测试用例信息
        self.rows = ReadExcel.get_rows()
        self.function_method = ReadExcel.get_col(9)
        self.running = ReadExcel.get_col(10)

    def test_Buyer(self,worksheet):
        '''运行excel里所有符合TestCase1方法且需运行的case'''
        global runcase
        for row in range(2, self.rows):
            # if self.running[row] == "Yes":
            if self.function_method[row] == "Yes" and self.running[row] == "Yes":

                runcase += 1
                print("runcase是：",runcase)
                BuyerTestCase(row).test_buyerCase(worksheet,runcase)
                log.info('*' * 100)
        report.close_workbook()






def main():
    log.info('开始测试')
    start = time.time()
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
    log.info('当前时间是：%s' % start_time)
    report.test_detail()
    report.init()
    sheet2=report.get_worksheet2()
    TestAllCase().test_Buyer(sheet2)

    end = time.time()
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end))
    log.info('当前时间是：%s' % end_time)
    log.info('耗时：%s' %(end - start))
    log.info('测试完毕')
if __name__ == '__main__':
    main()
