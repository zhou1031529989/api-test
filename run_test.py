# Author:Zhou Chao
import unittest
from common import c02_contants
from libext import HTMLTestRunnerNew

#自动查找testcases目录下，以test开头的.py文件里面的测试类
discover = unittest.defaultTestLoader.discover(c02_contants.testcases_dir, pattern="test_*.py", top_level_dir=None)

"""def discover(self,start_dir:str,pattern:str=...,
top_level_dir:Optional[str]=...) ->TestSuite:...

pattern： 正则
start_dir：从哪里开始找（根目录，或者子目录）
top_level_dir：如果只有一级目录，则如上，start_dir和top_level_dir是同一个
               如果testcases下面还有文件夹，文件夹里面还有文件夹，这种层级目录时，就要告诉函数，从哪个文件开始找，如果不传，默认是从根目录开始找
"""

with open(c02_contants.repores_html, 'wb+') as file:

    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title='API',
                                              description='API测试报告',
                                              tester='zhouchao')

    runner.run(discover)  # 执行查找到的用例



