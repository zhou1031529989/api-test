# -*- coding: utf-8 -*-
# @Time     : 2019/8/1 20:39
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : test_login.py
# @Software : 
import unittest

from libext.ddtnew import ddt,data
from common.c01_do_excel import DoExcel
from common import c02_contants
from common.c03_request import Request
from common import logger

logger = logger.get_logger(logger_name="LoginTest")

@ddt
class LoginTest(unittest.TestCase):

    do_excel = DoExcel(c02_contants.case_file) # 传入cases.xlsx
    cases = do_excel.read('login')
    request = Request() # 实例化对象

    def setUp(self):
        pass

    @data(*cases)
    def test_login(self,case):
            logger.info('开始执行第{0}条用例'.format(case.case_id))
            # 使用封装好的request 来完成请求
            resp = self.request.request1(case.method,case.url,case.data)   # request成为成员变量，用self调用
            # 将返回结果和期望结果进行匹配
            try:
                self.assertEqual(case.expected,resp.text,'login error')
                # 一致就写入Excel的结果为PASS
                self.do_excel.write_back('login',case.case_id+1,resp.text,'PASS')     # do_excel成为类变量，用self调用
                logger.info('第{0}条用例执行结果：PASS'.format(case.case_id))
            except AssertionError as e:
                self.do_excel.write_back('login',case.case_id+1,resp.text,'FAILED')
                logger.error('第{0}条用例执行结果：Failed'.format(case.case_id))
                raise e

    def tearDown(self):
        pass