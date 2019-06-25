#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''

__author__:'shimengqi'
__description__:'读取测试用例信息'
__mtime__:2018/2/1
'''

import xlrd
import  os
from readConfig import ReadConfig

ReadConfig = ReadConfig()



class ReadExcel:
    def __init__(self):
        '''打开工作表'''
        # 从配置文件获取测试用例地址
        data_address=ReadConfig.get_config("DATABASE","data_address")
        # data_address=os.path.abspath('../data/buyerdata1.xlsx')
        # 从excel提取测试用例信息
        workbook = xlrd.open_workbook(data_address)
        self.table = workbook.sheets()[0]

    def get_rows(self):
        '''获取工作表行数'''
        rows = self.table.nrows
        return rows

    def get_cell(self, row, col):
        '''获取单元格数据'''
        cell_data = self.table.cell(row, col).value

        return cell_data

    def get_col(self, col):
        '''获取整列数据'''
        col_data = self.table.col_values(col)
        return col_data



def main():
    excel_data = ReadExcel()
    print(excel_data.get_cell(3, 5))
    print(excel_data.get_rows())
if __name__ == '__main__':
    main()
