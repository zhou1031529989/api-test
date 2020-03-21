# -*- coding: utf-8 -*-
# @Time     : 2019/8/1 21:31
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : test_api.py
# @Software : 

import unittest
from common.c01_do_excel import DoExcel
from common import c02_contants
from common.c03_request import Request

from ddt import ddt,data

"""
1.数据库里面查最大的手机号+1
2.case.data里面的手机号码给替换掉
3.然后再去请求
"""
from common.c04_mysql import MysqlUtil
@ddt
class APITest(unittest.TestCase):

    do_excel = DoExcel(c02_contants.case_file) # 传入cases.xlsx
    login_cases = do_excel.read('login')
    register_cases = do_excel.read('register')
    request = Request() # 实例化对象

    @unittest.skip("不要运行")
    @data(*login_cases)
    def test_login(self,case):
            print('开始执行第{0}条用例'.format(case.case_id))
            # 使用封装好的request1 来完成请求
            resp = self.request.request1(case.method,case.url,case.data)
            # 将返回结果和期望结果进行匹配
            try:
                self.assertEqual(case.expected,resp.text,'login error')
                # 一致就写入Excel的结果为PASS
                self.do_excel.write_back('login',case.case_id+1,resp.text,'PASS') #类变量，用self调用
                print('第{0}条用例执行结果：PASS'.format(case.case_id))
            except AssertionError as e:
                self.do_excel.write_back('login',case.case_id+1,resp.text,'FAILED')
                print('第{0}条用例执行结果：Failed'.format(case.case_id))
                raise e

    def setUp(self):

        mysql = MysqlUtil()                                          # 创建数据连接
        self.sql = "select max(mobilephone) from future.member"    # 查询最大手机号  # 最大手机号为18999999999时，再加1成19000000000就不再是手机号码了，要删数据
        self.max= mysql.fetch_one(self.sql)[0]                       # 值为元祖，根据下标取到电话号码
        print(type(max))
    @data(*register_cases)
    def test_register(self,case):
            print('开始执行第{0}条用例'.format(case.case_id))
            import json
            data_dict = json.loads(case.data)
            if data_dict['mobilephone'] == '${register_mobile}':
                data_dict['mobilephone'] = int(self.max) + 1
            # 使用封装好的request 来完成请求
            resp = self.request.request1(case.method,case.url,data_dict)
            # 将返回结果和期望结果进行匹配
            try:
                self.assertEqual(case.expected,resp.text,'register error')
                # 一致就写入Excel的结果为PASS
                self.do_excel.write_back('register',case.case_id+1,resp.text,'PASS') #类变量，用self调用
                print('第{0}条用例执行结果：PASS'.format(case.case_id))
            except AssertionError as e:
                self.do_excel.write_back('register',case.case_id+1,resp.text,'FAILED')
                print('第{0}条用例执行结果：Failed'.format(case.case_id))
                raise e


