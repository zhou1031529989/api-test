import pymysql
from common.c05_config import ReadConfig

class MysqlUtil:

    def __init__(self,return_dict=False):

        # host="test.lemonban.com"
        # user="test"
        # password="test"
        # 将上面的那块，放进配置文件
        config = ReadConfig()
        host = config.get('db','host')
        user = config.get('db','user')
        password = config.get('db','pwd')
        port = config.getint('db','port')

        #1.建立连接
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)
        #2.新建一个查询
        if return_dict:
            self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor) #指定每行数据以字典的形式返回
        else:
            self.cursor = self.mysql.cursor() #指定每行数据以元祖的形式返回

    def fetch_one(self,sql):#查询
        #执行
        self.cursor.execute(sql)
        #获取结果,
        result = self.cursor.fetchone()#返回元祖（）
        return result

    # 存在多条数据时，注册多个数据等
    def fetch_all(self,sql):
        #执行SQL
        self.cursor.execute(sql)
        #获取结果
        results = self.cursor.fetchall()#返回列表[(),()]
        return results

    def close(self):
        self.cursor.close()#关闭查询
        self.mysql.close()#关闭连接

if __name__ == '__main__':
    # mysql = MysqlUtil()
    # sql = "select max(mobilephone) from future.member"
    # result= mysql.fetch_one(sql)#返回tuple
    # print(result[0])#根据下标取值
    # mysql.close()

    mysql = MysqlUtil(return_dict=True)
    sql = "select * from future.member limit 10"
    results = mysql.fetch_all(sql)#返回列表里面放dictionary
    for result in results:
        #print(result)
        print(result['Id'])
    mysql.close()
