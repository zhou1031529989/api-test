# s 是目标字符串
# d 是替换的内容
# 找到目标字符串里面的标识符KEY，去d里面拿到替换的值
# 替换到s里面去，然后再返回
import re
from common.c05_config import ReadConfig
config = ReadConfig()
# 上下文类，数据的准备和记录，利用反射根据类动态获取属性值
class Context:
    admin_user = config.get('data','admin_user')
    admin_pwd = config.get('data','admin_pwd')
    loan_member_id = config.get('data','loan_member_id')
    # loan_id  运行完加标后，动态给Context加上这个属性，不是一开始就有的，所有不定义成类属性
    normal_user = config.get('data','normal_user')
    normal_pwd = config.get('data','normal_pwd')
    normal_member_id = config.get('data','normal_member_id')

# 正则
def replace(s,d):
    p = "\$\{(.*?)}"
    while re.search(p, s):
        m = re.search(p, s)
        key = m.group(1)
        value = d[key]
        s = re.sub(p, value, s, count=1)
    return s

data = {"admin_user":"15873171553","admin_pwd":"123456"}
# s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
#
# s = replace(s,data)
# print(s)

# ￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥4
# 反射
def replace_new(s):
    p = "\$\{(.*?)}"
    while re.search(p, s):
        m = re.search(p, s)
        key = m.group(1)
        if hasattr(Context, key):
            value = getattr(Context, key)        # 利用反射动态的获取属性
            s = re.sub(p, value, s, count=1)
        else:
            return None                        # 返回None,或者抛出一个异常，告知没有这个属性
    return s

s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'

s = replace_new(s)
print(s)

