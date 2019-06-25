import xlrd
import  os
from readConfig import ReadConfig

ReadConfig = ReadConfig()

class ReadExcelData:
    def __init__(self):
        '''打开工作表'''
        # 从配置文件获取测试用例地址
        data_address=ReadConfig.get_config("DATABASE","data_address")
        # data_address=os.path.abspath('../data/buyerdata1.xlsx')
        # 从excel提取测试用例信息
        workbook = xlrd.open_workbook(data_address)
        self.table = workbook.sheets()[0]
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.RowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def getRowData(self):
        if self.RowNum<=1:
            print("总行数小于1")
        else:
            r=[]
            j=1
            for i in range(self.RowNum-1):
                s={}
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                    print(s[self.keys[x]] )


                r.append(s)
                j += 1
            return r



def main():
    a=ReadExcelData()
    a.getRowData()

if __name__=='__main__':
    main()
















