# Author:Zhou Chao

from common.c01_do_excel import DoExcel

from common.c03_request import Request
from libext.ddtnew import ddt, data
from common.c04_mysql import MysqlUtil


from common import logger
from common import c02_contants

logger = logger.get_logger(logger_name='case')

import unittest

@ddt
class TestRegister(unittest.TestCase):
    do_excel=DoExcel(c02_contants.case_file)
    register_test_data=do_excel.read('register')
    request=Request()

    def setUp(self):

        self.mysql = MysqlUtil(return_dict=True)  # 创建数据连接
        sql = "select max(mobilephone) as max_phone from future.member"  # 查询最大手机号
        self.max= self.mysql.fetch_one(sql)['max_phone']  # 值为元祖，根据下标取到电话号码

    @data(*register_test_data)
    def test_register(self,case):
            #参数的处理
            logger.info('开始执行第{0}条用例'.format(case.case_id))
            data = case.data
            import json
            data = json.loads(data) # 返回一个字典
            if data['mobilephone'] == '${register_mobile}':  # 根据key，进行替换
                data['mobilephone'] = int(self.max)+1
            # 使用封装好的request1来完成请求
            resp= self.request.request1(case.method,case.url,data)   # data 转换出来的字典传进去
            try:
                self.assertEqual(case.expected,resp.text,'register error')

                # 数据库查询数据校验
                # 注册成功，手机号等于注册时的手机号data['mobilephone']
                if resp.json()['msg'] == '注册成功':
                    sql = 'select * from future.member where mobilephone = {0} '\
                          .format(data['mobilephone'])
                    results = self.mysql.fetch_all(sql)
                    # 1.首先判断是否有成功插入数据，判断列表的长度，注册成功就会有一条数据
                    self.assertEqual(1,len(results))
                    member = results[0]                        # 获取到这一条数据，是一个字典
                    # 2.判断注册成功余额应该是0
                    self.assertEqual(0,member['LeaveAmount'])
                    # 3.判断会员的类型Type（0,1,2）
                    # 4.判断昵称，传进来的名字或者是默认的昵称

                self.do_excel.write_back('register',case.case_id+1,resp.text,'PASS')
                logger.info('第{0}条用例执行结果：PASS'.format(case.case_id))
            except AssertionError as e:
                self.do_excel.write_back('register',case.case_id+1,resp.text,'FAILED')
                logger.error('第{0}条用例执行结果：Failed'.format(case.case_id))
                raise e

    def tearDown(self):
        self.mysql.close()