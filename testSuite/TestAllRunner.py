#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'shimengqi'
__description__:'创建多线程(貌似没用)'
__mtime__:2017/3/8
'''

import time
import threading
from log import Log
from readConfig import ReadConfig
from TestSuite import TestAllCase

log=Log()
ReadConfig=ReadConfig()
class TestAllRunner:
    def threads(self,worksheet):
        hthreads=[]#创建线程数组
        hthreads.append(threading.Thread(target=TestAllCase().test_Buyer(worksheet)))
        # hthreads.append(threading.Thread(target=TestAllCase().test_BuyerWithootParam(worksheet)))
        for h in hthreads:
            h.start()#开始线程活动
            h.join()#把主线程挂起，等上面的线程跑完了再运行

def main():
    log.info("开始测试")
    start=time.time()
    start_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
    log.info("当前时间是%s"%start_time)
    Runner=TestAllRunner()
    Runner.threads()
    end=time.time()
    end_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(start))
    log.info("当前时间是%s"%end_time)
    log.info("耗时是%s"%(end-start))
    log.info("测试完毕")

if __name__ == '__main__':
    main()















