from common.c01_do_excel import DoExcel
from common import c02_contants
from common.c03_request import Request

do_excel = DoExcel(c02_contants.case_file)
test_data = do_excel.read('login')
request = Request() #
for case in test_data:
    #参数的处理
    print('开始执行第{0}条用例'.format(case.case_id))
    resp = request.request1(case.method,case.url,case.data)
    print('method',case.method)
    print('url',case.url)
    print('data',case.data)
    print(resp.json())
    if resp.text == case.expected:
        do_excel.write_back('login',case.case_id+1,resp.text,'PASS')
        print('第{0}条用例执行结果：PASS'.format(case.case_id))
    else:
        do_excel.write_back('login',case.case_id+1,resp.text,'FAILED')
        print('第{0}条用例执行结果：Failed'.format(case.case_id))

