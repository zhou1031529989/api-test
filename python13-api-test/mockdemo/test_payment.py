# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function：
支付测试类：
1，正确的用户信息，支付成功
2，正确用户信息，支付失败
3，超时，超时再成功
4，超时，超时再失败
"""
import unittest
from unittest import mock
from mockdemo import payment

class PaymentTest(unittest.TestCase):

    def setUp(self):
        self.payment = payment.Payment()

    def test_01_success(self):
        # mock requestOutofSystem方法，模拟返回状态码是200（所以self.payment.requestOutofSystem后面没有()）
        self.payment.requestOutofSystem = mock.Mock(return_value=200)
        resp = self.payment.doPay(user_id=1, card_num='123456', amount=100)
        self.assertEqual('success', resp)

    def test_02_fail(self):
        self.payment.requestOutofSystem = mock.Mock(return_value=500)
        resp = self.payment.doPay(user_id=2, card_num='1234567', amount=100.01)
        self.assertEqual('fail', resp)

    def test_03_retry_success(self):
        # side_effect 必须是元祖、列表,str,字典,对象等iterate可迭代数据类型
        self.payment.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 200])  # 第一次返回TimeoutError，第二次返回200
        resp = self.payment.doPay(user_id=3, card_num='12345678', amount=10.01)
        print(resp)
        self.assertEqual('success', resp)

        # 判断mock方法被如何调用       #判断调用了正确的参数
        self.payment.requestOutofSystem.assert_called_with(user_id=3, card_num='12345678', amount=10.01)

    def test_04_retry_fail(self):
        self.payment.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 500])
        resp = self.payment.doPay(user_id=4, card_num='123445789', amount=0.01)
        print(resp)
        self.assertEqual('fail', resp)

        print('requestOutofSystem被调用次数：',self.payment.requestOutofSystem.call_count)
