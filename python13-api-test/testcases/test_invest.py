import unittest

from common.c01_do_excel import DoExcel
from common import c02_contants,logger
from common.c03_request import Request
from libext.ddtnew import ddt, data
from common import c06_context
from common.c04_mysql import MysqlUtil
from common.c06_context import Context

logger = logger.get_logger(logger_name='case')  # 获取log实例

# 1.excel里面设计第一条case是正常登陆
# 2.session 保持会话的方式来进行请求的话，那就需要你把这个request的实例化的对象放到类里面
# 3.获取Excel数据，运行用例

@ddt
class TestInvest(unittest.TestCase):
    do_excel = DoExcel(c02_contants.case_file)
    invest_test_data = do_excel.read('invest')

    @classmethod
    def setUpClass(cls):
        logger.debug('\n这是一个类方法')
        cls.request = Request()  #
        cls.mysql = MysqlUtil()

    def setUp(self):
        logger.debug('这是一个setup方法')
        print()
        pass

    @data(*invest_test_data)
    def test_invest(self, case):
        # 参数的处理
        logger.info('开始执行第{0}条用例'.format(case.case_id))
        # 查找参数化的测试数据，动态替换
        data_new = c06_context.replace_new(case.data)   # Str测试数据
        # 使用封装好的request1，来完成请求
        resp = self.request.request1(case.method, case.url, data_new)

        try:
            null = ""   # 防止跑run_test.py时，出错，NameError:has no null

            if type(eval(case.expected)) is int:
                self.assertEqual(case.expected, resp.json()['code'], 'invest error')
            else:
                self.assertEqual(case.expected, resp.text, 'invest error')

            self.do_excel.write_back('invest', case.case_id + 1, resp.text, 'PASS')
            logger.info('data_new的类型', type(data_new), data_new)
            logger.info('第{0}条用例执行结果：PASS'.format(case.case_id))
            # 判断是否加标成功，如果成功就按照借款人ID去数据库查询最新标的记录
            if resp.json()['msg'] == '加标成功':
                loan_member_id = getattr(Context,'loan_member_id')
                sql = "select * from future.loan where memberID='{0}'" \
                      "ORDER BY createtime DESC limit 1".format(loan_member_id)
                loan_id = self.mysql.fetch_one(sql)[0]
                setattr(Context,'loan_id',str(loan_id))  # 记得转成字符串，后续通过正则替换

            # 数据库的校验
            if resp.json()['msg'] == '竞标成功':
                # 1.账户余额
                # 2.标的余额，在投资记录里
                # 3.投资记录
                pass

        except AssertionError as e:
            self.do_excel.write_back('invest', case.case_id + 1, resp.text, 'FAILED')
            logger.error('第{0}条用例执行结果：Failed'.format(case.case_id))
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session
        cls.mysql.close()            # 关闭数据库
