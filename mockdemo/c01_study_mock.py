# Author:Zhou Chao

from unittest import mock
import requests

def request_baidu():
    # 抓百度的内容,text是HTML类型的
    return requests.get('http://www.baidu.com').text.encode('utf-8')

def print_baidu():
    print(request_baidu())

# 直接返回百度的内容
# print_baidu()

# mock返回this is baidu.
request_baidu = mock.Mock(return_value='this is baidu.')
print_baidu()

