import os

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#python13项目根路劲

print(base_dir)

data_dir=os.path.join(base_dir,"datas")
case_file=os.path.join(data_dir,"testcase.xlsx")#拼接获取测试用例文件

print(case_file)

conf_dir = os.path.join(base_dir,"conf")  # 先找到conf文件夹所在路径
test_conf = os.path.join(conf_dir,"test.conf")  # 再拼接配置文件的路径
test2_conf = os.path.join(conf_dir,"test2.conf")
global_conf = os.path.join(conf_dir,"global")

# log文件路径
logs_dir = os.path.join(base_dir,"logs")

# 测试文件路径
testcases_dir = os.path.join(base_dir,"testcases")

reports_dir = os.path.join(base_dir,'reports')          # reports文件夹路径
repores_html = os.path.join(reports_dir,'reports.html') # reports文件路径