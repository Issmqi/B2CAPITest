#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'shimengqi'
__description__:'从登录接口获取token'
__mtime__:2018/1/17
'''


from readConfig import ReadConfig

ReadConfig = ReadConfig()

class GetToken:

    def getBuyertoken(self):

        '''获取登录的token'''
        token=ReadConfig.get_config("DATABASE","token")
        print(token)
        return token

def main():
    tokendata = GetToken()
    tokendata.getBuyertoken()
if __name__ == '__main__':
    main()