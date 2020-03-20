import unittest

from common.c01_do_excel import DoExcel
from common import c02_contants
from common.c03_request import Request
from libext.ddtnew import ddt, data


# 1.excel里面设计第一条case是正常登陆
# 2.session 保持会话的方式来进行请求的话，那就需要你把这个request的实例化的对象放到类里面
# 3.获取Excel数据，运行用例

@ddt
class TestRecharge(unittest.TestCase):
    do_excel = DoExcel(c02_contants.case_file) #类属性，传入cases.xlsx
    recharge_test_data = do_excel.read('recharge')

    @classmethod
    def setUpClass(cls): # 继承unittest.TestCase里面的类方法，每个测试类里面去运行的操作，放到类方法里面
        print('\n这是一个类方法')
        cls.request = Request()  # 实例化一个Request类对象 # 类方法，只执行一次，整个类只执行一次
                                 # cls.request 类变量，相当于TestCase,是一个类名
    def setUp(self):
        # 每个测试方法里面去运行的操作，放到测试方法里面
        print('这是一个setup方法') # 用例方法，每个用例执行一次
        print()

    @data(*recharge_test_data)
    def test_recharge(self, case):
        # 参数的处理
        print('开始执行第{0}条用例'.format(case.case_id))
        # self.request类实例，既可以获取类变量，又可以获取实例变量
        resp = self.request.request1(case.method, case.url, case.data)
        print(resp.json())
        try:
            # resp.json() 把resp.text返回的字符串转成字典，用code这个key去取值
            self.assertEqual(case.expected, resp.json()['code'], 'recharge error')
            self.do_excel.write_back('recharge', case.case_id + 1, resp.text, 'PASS')
            print('第{0}条用例执行结果：PASS'.format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_back('recharge', case.case_id + 1, resp.text, 'FAILED')
            print('第{0}条用例执行结果：Failed'.format(case.case_id))
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close() # 用完后关闭session会话
