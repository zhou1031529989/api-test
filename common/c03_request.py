import requests
from common.c05_config import ReadConfig
from common import logger

logger = logger.get_logger('request1')

class Request:

    def __init__(self):
        self.session=requests.sessions.Session()   # 实例化一个session

    def request1(self,method,url,data=None):
        method = method.upper()   # 将字符全部转换成大写

        config = ReadConfig()
        pre_url = config.get('api','pre_url') # 拼接
        url = pre_url+url

        if data is not None and type(data) == str:
            data=eval(data)   # 如果是字符串就转成字典
        logger.info('method:{0} url:{1}'.format(method, url))
        logger.info('data:{0}'.format(data))

        if method =='POST':
            resp = self.session.request(method,url=url,data=data)
            logger.info('response:{0}'.format(resp.text))
            return resp

        elif method=='GET':
            resp = self.session.request(method,url=url,params=data)
            logger.info('resoponse:{0}'.format(resp.text))
            return resp

        else:
            logger.error('Un-support method !!!')

    def close(self):
        self.session.close()  #关闭session

# DoExcel 有两个方法，一个是读，返回case列表，一个是写
# 1，先实例化一个DoExcel 对象
# 2，然后用这个实例对象去获取cases列表
# 3, 使用requests 去完成接口的调用，拿到返回
# 4，拿到期望结果和实际结果判断
# 5，还是使用之前的实例对象，调用写的方法，回写到Excel里面去











