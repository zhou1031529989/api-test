import configparser
from common import c02_contants

class ReadConfig:

    def __init__(self):
        # 实例化对象
        self.config = configparser.ConfigParser()
        # 加载文件
        self.config.read(c02_contants.global_conf, encoding='utf-8') # 先加载开关的配置
        open = self.config.getboolean('switch','open')  # 获取配置文件项里的值,

        if open:
            self.config.read(c02_contants.test_conf, encoding='utf-8') # 再加载测试环境数据库schema
        else:
            self.config.read(c02_contants.test2_conf, encoding='utf-8')

    def get(self,section,option):   # 封装config.get方法，外部调用时直接调用自己的get方法(read_config.get)就相当于调用ConfigParser类的get方法 （如：read_config.config.get()）
        return self.config.get(section,option)

    def getboolean(self,section,option):
        return self.config.getboolean(section,option)

    def getint(self,section,option):
        return self.config.getint(section,option)

if __name__ == '__main__':
    read_config = ReadConfig()
    print(read_config.get('api','pre_url'))
    print(read_config.getint('db','port'))