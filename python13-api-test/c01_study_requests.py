'''
HTTP 协议两大部分
{Request:入参}
·请求方法：
GET     查--获取资源
POST    改---修改资源(增加或者修改资源) 需要传参
PUT     增加 需要传参
DELETE  删除 需要传参
OPTION （获取可以支持的请求方式[后端方法]）
HEADER  返回请求和response的头部信息（无返回体）

·请求URL：  协议://服务器IP地址:端口号/接口路径
           协议://域名/接口路径

·请求参数：传参方式有两种 URL 表单

·header 请求头： Content-type    User-Agent（请求端信息[请求由谁发起] 如：APP手机版本信息 浏览器信息 请求模拟时可以自己设置User-Agent）
（按照接口的要求告诉服务器我传的Content-Type是什么样的格式）

·cookie（web保存的信息 用户信息 缓存 登录时效 cookies在客户端，服务器端返回给客户端，保存到本地，下次请求带过去的标识）

{Response:出参}
·状态码：
1XX——信息类（Information）,表示收到Web浏览器请求，正在进一步的处理中
2XX——成功类（Successful），表示用户请求被正确接收，理解和处理（未必处理），例如：200 OK
(200只表示接口调用成功，不代表实际功能正确，需要校验响应数据/数据库的数据，才是准确的)
3XX——重定向类（Redirection）,表示请求没有成功，客户必须采取进一步的动作。
4XX——客户端错误（Client Error），表示客户端提交的请求错误 例如：404 NOT Found。
5XX——服务器错误（Server Error），表示服务器不能完成对请求的处理 如：500

·响应信息：（响应body）【接口测试第一步判断状态码，第二步判断响应信息，第三步判断数据库】

·cookie（客户端发出的请求到服务端，服务端将产生的cookies通过response的cookies传递给客户端）
（认权 会放在head里面）
（或者返回，到响应信息里面）

·header：（告诉客户端返回回来的信息有什么要求和格式，信息从哪里来的）
Server -->
Data -->
Content-Type -->
Transfer-Encoding -->
Connection -->
Set-Cookie -->
Set-Cookie -->

{http请求的过程}
按照接口的定义（接口的请求方式post get ... 接口的URL） 传参（body params） ，告诉你我的请求信息（header）
服务端拿到请求，返回相应的响应信息

'''

"""
使用requests完成其中注册，登录，充值接口的调用 （充值需要传登录之后返回的cookies）

# requests文档参考：（其中快速上手都照着练习一下，你会发现对requests摸得透透的！）

# http://cn.python-requests.org/zh_CN/latest/
"""


import requests


#注册接口

data = {'mobilephone':'15201942869','pwd':'1234567890',"regname":"小秘shu"}
resp=requests.post('http://test.lemonban.com/futureloan/mvc/api/member/register',data=data)
# print('请求信息',resp.request.url)
# print('请求参数',resp.request.body)
# print('请求headers',resp.request.headers)
# print('请求cookies',resp.request._cookies)
#
# print('响应码',resp.status_code)
# print('响应信息',resp.text)
#
# print('响应信息类型',type(resp.text))
# print('响应信息字典',resp.json())
# print('响应信息字典类型',type(resp.json()))
# print('响应信息字典',resp.json()['status'])
#
# print('响应cookis',resp.cookies)
# print('响应headers',resp.headers)
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # 1.构造请求
# resp = requests.get('http://cn.python-requests.org/zh_CN/latest/')    # 请求方法requests.get  请求URL 请求参数params=None 动态参数暂时不用
# # 查看返回的信息，用变量resp接收返回，返回HTML，所有的返回内容都在对象resp里面
# print('响应码',resp.status_code)   # 根据对象的属性获取内容
# print('响应信息',resp.text)
# # 将HTML保存到一个文件index.html中,通过浏览器将index.html打开
# with open('index.html','w+',encoding='utf-8') as file:
#     file.write(resp.text)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 《get 则用params》
# 《post put delete 就用data》

# 登录接口 get----url传参 要用params传参，关键字传参
# data = {'mobilephone':'15810447656','pwd':'123456'}
# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login',params=data)#params url传参 拼接到URL路径下
# print('请求URL',resp.request.url)
# print('请求参数',resp.request.body)
# print('响应码',resp.status_code)
# print('响应信息',resp.text)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 登录接口 post----表单传参 用data传参 ，需要使用字典
data = {'mobilephone':'15810447656','pwd':'123456'}
resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login',data=data)#data 表单传参
print('请求URL',resp.request.url)
print('请求参数',resp.request.body)
print('请求headers',resp.request.headers)
print('请求cookies',resp.request._cookies)  # protected属性需要在前面加_（debug查看对象resp下面请求信息request所有属性的类型和值）（其他的则是resp的响应信息）

print('响应码',resp.status_code)
print('响应信息',resp.text)

print('响应信息类型',type(resp.text))
#将响应信息转化为字典
print('响应信息字典',resp.json())
#响应字典类型
print('响应信息字典类型',type(resp.json()))
#通过将响应信息转化为字典，可以查看key对应的value值
print('响应信息字典',resp.json()['status'])

print('响应cookis',resp.cookies) # 是一个对象
print('响应headers',resp.headers)


# 数据管理和数据驱动
# 测试脚本与测试数据的分离，降低维护成本，迁移成本以及提高效率！
# 1.基础数据（数据库连接参数、环境参数）：写入到配置文件
# 2.测试数据（不同组合参数组合，每个接口的数据格式是一样，针对不同的场景，我们需要准备不同的值）：写入到文件当中，json,exccel,csv
# ·json（少量数据）比较推荐，可以存储多个字段，解析也方便快捷，便于维护，但数据不太直观，不便于结果的回写；
# ·Exce（大量数据）推荐，可以存储多个字段，数据直观，便于结果好状态的回写，但读写解析相对来说要麻烦些；
# ·数据库（百条以上测试用例）
# 1）临时数据，只是使用一次的数据，建议直接写入到脚本中。


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 充值接口 post----表单传参 用data传参
data_2 = {'mobilephone':'15201942863','amount':1}
resp_2=requests.post('http://test.lemonban.com/futureloan/mvc/api/member/recharge',data=data_2)#params url传参
print('响应信息',resp_2.text)
# resp_2.encoding='utf-8'#解决乱码问题
# print('请求信息',resp_2.request.url)
# print('请求参数',resp_2.request.body)
# print('请求headers',resp_2.request.headers)
# print('请求cookies',resp_2.request._cookies)
#
# print('响应码',resp_2.status_code)


# print('响应信息类型',type(resp_2.text))
# print('响应信息字典',resp_2.json())
# print('响应信息字典类型',type(resp_2.json()))
# print('响应信息字典',resp_2.json()['status'])
#
# print('响应cookis',resp_2.cookies)
# print('响应headers',resp_2.headers)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#投资接口
#
data_3 = {'memberId':1115608,'password':'1234567890','loanId':4822,'amount':100}
resp_3=requests.post('http://test.lemonban.com/futureloan/mvc/api/member/bidLoan',data=data_3)#params url传参
#
# print('响应信息',resp_3.text)



#提现接口

data_4 = {'mobilephone':'15201942869','amount':123.5}
resp_4 = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/withdraw',data=data_4)
