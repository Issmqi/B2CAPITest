import time
import os
import xlsxwriter
from log import Log
from readConfig import ReadConfig

log=Log()
ReadConfig=ReadConfig()
hpassnum=0

class Report:
    def __init__(self):
        '''从config.ini读取数据'''
        # 获取项目绝对路径
        report_address=os.path.abspath('../testReport/report/')+'\\'
        # report_address=ReadConfig.get_config("DATABASE","report_address")
        self.project_name=ReadConfig.get_config("TABLEDATA","project_name")
        self.version = ReadConfig.get_config("TABLEDATA","version")
        self.scripting_language = ReadConfig.get_config("TABLEDATA","scripting_language")
        self.internet =ReadConfig.get_config("TABLEDATA","internet")
        self.now = time.strftime("%Y-%m-%d-%H-%M-%S ", time.localtime(time.time()))
        self.report=report_address+self.now+'report.xlsx'
        self.workbook=xlsxwriter.Workbook(self.report)#生成测试报告
        self.worksheet=self.workbook.add_worksheet("测试总况")
        self.worksheet2=self.workbook.add_worksheet("测试详情")

    def get_workaddress(self):
        '''获取生成的excel地址'''
        return self.report
    def get_worksheet(self):
        '''获取sheet'''
        return self.worksheet
    def get_worksheet2(self):
        '''获取sheet2'''
        return self.worksheet2
    def set_format(self,font_size=14, bg_color='#B0E0E6', font_color='#000000', num=1):
        '''
                设置单元格样式
                font_size: 字体大小（默认12号
                bg_color: 背景色值（默认豆绿色）
                font_color: 字体色值（黑色）
                num: 是否有边框（1表示有）
                '''
        cell_style = self.workbook.add_format(
            {'align': 'center', 'valign': 'vcenter', 'border': num, 'font_size': font_size, 'bg_color': bg_color,
             'font_color': font_color})
        return cell_style
    def write_cell(self,worksheet,c1,data):
        '''
        单元格写入数据
        :param worksheet: 工作表
        :param c1: 单元格
        :param data: 数据
        :return:
        '''
        return worksheet.write(c1,data,self.set_format())
    def write_area(self,worksheet,c1,data,sign):
        '''
        合并多个单元格写入数据
        :param worksheet:
        :param c1:
        :param data:
        :param sign:
        :return:
        '''
        return worksheet.merge_range(c1,str(round(data,2))+sign,self.set_format())
    def write_basic(self,caseId,caseName,APIName,url,method,data,expectCode,worksheet,temp):
        '''
        把基本数据写入excel
        :param caseId:
        :param testAPI:
        :param caseName:
        :param url:
        :param method:
        :param data:
        :param ExpectCode:
        :param worksheet:
        :param temp:写入的行数
        :return:
        '''
        item = {"t_id": caseId, "t_name": caseName,"t_api":APIName, "t_url": url,"t_method": method,
                "t_param": '%s' % data, "t_hope": 'code: %s' % expectCode}
        self.write_cell(worksheet, "A" + str(temp), item["t_id"])
        self.write_cell(worksheet, "B%s" % temp, item["t_name"])
        self.write_cell(worksheet, "C%s" %temp , item["t_api"])
        self.write_cell(worksheet, "D%s" % temp, item["t_url"])
        self.write_cell(worksheet, "E%s" % temp, item["t_method"])

        self.write_cell(worksheet, "F%s" % temp, item["t_param"])
        self.write_cell(worksheet, "G%s" % temp, item["t_hope"])
    def write_special(self,actual,ExpectCode,worksheet,temp):
        '''
        把结果写入excel
        :param actual: 实际结果
        :param ExpectCode: 预期code
        :param worksheet: 工作表
        :param temp: 写入行
        :return:
        '''
        if actual=={}:
            self.write_cell(worksheet,"H%s"%temp,"返回结果缺失")
            self.write_cell(worksheet,"I%s"%temp,"失败")
        elif actual['code']==ExpectCode:
            self.write_cell(worksheet,"H%s"%temp,"resCode:%s,msg%s"%(actual['code'],actual['msg']))
            self.write_cell(worksheet,"I%s"%temp,"成功")
        elif actual['code']!=ExpectCode:
            self.write_cell(worksheet, "H%s" % temp, "resCode:%s,msg%s" % (actual['code'], actual['msg']))
            self.write_cell(worksheet, "I%s" % temp, "失败")
    def init(self):
        '''
        创建项目总况表结构
        :return:
        '''

        # 设置列宽
        self.worksheet.set_column("A:A",15)
        self.worksheet.set_column("B:B",20)
        self.worksheet.set_column("C:C", 20)
        self.worksheet.set_column("D:D", 20)
        self.worksheet.set_column("E:E", 20)
        self.worksheet.set_column("F:F", 20)


        # 设置行高
        for hrow in range(6):
            self.worksheet.set_row(hrow, 30)

        # 生成工作表内容
        self.worksheet.merge_range('A1:G1','测试报告总况',self.set_format(18,"#CAE1FF"))
        self.worksheet.merge_range('A2:G2','测试概况',self.set_format(16, "#ADD8E6", "#ffffff"))
        self.worksheet.merge_range('A3:A6','接口自动化',self.set_format())
        self.write_cell(self.worksheet,'B3','项目名称')
        self.write_cell(self.worksheet,'B4','接口版本')
        self.write_cell(self.worksheet, 'B5', '脚本语言')
        self.write_cell(self.worksheet, 'B6', '网络环境')
        self.write_cell(self.worksheet,'C3',self.project_name)
        self.write_cell(self.worksheet, 'C4', self.version)
        self.write_cell(self.worksheet, 'C5', self.scripting_language)
        self.write_cell(self.worksheet, 'C6', self.internet)
        self.write_cell(self.worksheet, "D3", "测试用例总数")
        self.write_cell(self.worksheet, "D4", "通过总数")
        self.write_cell(self.worksheet, "D5", "失败总数")
        self.write_cell(self.worksheet, "D6", "报告时间")
        self.write_cell(self.worksheet, "E6", self.now)
        self.write_cell(self.worksheet, "F3", "耗时")
        self.write_cell(self.worksheet, "G3", "通过率")
        log.info("测试总况表创建成功")
        self.pie()


    def pie(self):
        '''生成饼状图'''
        chart1 = self.workbook.add_chart({'type': 'pie'})
        chart1.add_series({'name': '接口测试统计', 'categories': '=测试总况!$D$4:$D$5', 'values': '=测试总况!$E$4:$E$5', })
        chart1.set_title({'name': '接口测试统计'})
        chart1.set_style(3)     # 饼状图样式
        self.worksheet.insert_chart('A9', chart1, {'x_offset': 180, 'y_offset': 10})
        log.info('饼状图生成成功')

    def test_detail(self):
        '''创建测试详情表'''

        # 设置列宽
        self.worksheet2.set_column("A:A", 20)
        self.worksheet2.set_column("B:B", 20)
        self.worksheet2.set_column("C:C", 20)
        self.worksheet2.set_column("D:D", 20)
        self.worksheet2.set_column("E:E", 20)
        self.worksheet2.set_column("F:F", 20)
        self.worksheet2.set_column("G:G", 20)
        self.worksheet2.set_column("H:H", 20)
        self.worksheet2.set_column("I:I", 20)
        # 设置行高
        self.worksheet2.set_row(0, 50)
        self.worksheet2.set_row(1, 40)

        # 生成工作表内容
        self.worksheet2.merge_range('A1:I1', '测试详情', self.set_format(16, "#ADD8E6", "#ffffff"))
        self.write_cell(self.worksheet2, "A2", '用例ID')
        self.write_cell(self.worksheet2, "B2", '接口名称')
        self.write_cell(self.worksheet2, "C2", '用例名称')
        self.write_cell(self.worksheet2, "D2", 'URL')
        self.write_cell(self.worksheet2, "E2", '接口方法')
        self.write_cell(self.worksheet2, "F2", '参数')
        self.write_cell(self.worksheet2, "G2", '预期结果')
        self.write_cell(self.worksheet2, "H2", '实际结果')
        self.write_cell(self.worksheet2, "I2", '测试结果')
        log.info("测试详情表创建成功")
    def close_workbook(self):
        self.workbook.close()
        log.info("工作表关闭完毕")
def main():
    a=Report()
    a.test_detail()
    a.init()
    x=a.get_worksheet()
    a.write_area(x, 'F4:F6', 2, '*')
    a.close_workbook()


if __name__ == '__main__':
    main()


































