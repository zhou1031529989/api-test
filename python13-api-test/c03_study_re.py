#方法一

import json
import re      # 正则

# admin_user = '15873171553'
# admin_pwd = '123456'
# s = '{"mobilephone": "${admin_user}","pwd":"${admin_pwd}"}'
# 老方法，利用json，将字符串转成字典，然后根据key去取值，取到值判断是否需要替换
# dict1 = json.loads(s)
# if dict1['mobilephone'] == '${admin_user}':
#     dict1['mobilephone'] = admin_user
#
# if dict1['pwd'] == '${admin_pwd}':
#     dict1['pwd'] = admin_pwd
#
# print(dict1)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

data = {"admin_user":"15873171553","admin_pwd":"123456"}
s = '{"mobilephone": "${admin_user}","pwd":"${admin_pwd}"}'
p = "\$\{admin_user}"    # 匹配原本字符的写法 $需用转义符\$\
p1 = "\$\{(.*?)}"        # ()代表组，开始为${，结束为}      .匹配任意一个字符，*匹配多次，?至多匹配一次出来（不加?匹配结果为match='${admin_user}","pwd":"${admin_pwd}"}'）
                         # 正则匹配，元字符和限定符
m = re.search(p1, s)     # 任意位置开始找，找到一个就返回match
# n = re.search(p,s)
print("任意位置开始找，找到一个就返回match：",m)
# print("任意位置开始找，找到一个就返回match：",n)

g = m.group()     # 返回的是整个匹配的字符串
print(g)
g1 = m.group(1)   # 取第一个组的匹配字符串
print(g1)

l = re.findall(p1, s)   # 查找全部，并返回一个列表
print("查找全部，返回一个列表",l)

value = data[g1]  # data里面第一个key就是，g1的值
# s = s.replace('${admin_user}',value)    # 字符串函数方式，s里面mobilephone的值可以配替换掉
# print(s)
s = re.sub(p1, value, s, count=1)         # 查找全部 且替换,在字符串s里面，使用value替换正则表达式p1，count=0默认匹配全部
print("使用正则表达式查找，并且替换：", s)

