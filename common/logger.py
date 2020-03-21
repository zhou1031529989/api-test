# Author:Zhou Chao

import logging
import logging.handlers
import os
from common import c02_contants
from common.c05_config import ReadConfig

config = ReadConfig()

def get_logger(logger_name):
    # 创建一个日志收集器getLogger 函数
    logger = logging.getLogger(logger_name)
    # 设置收集器级别，设置为最低
    logger.setLevel('DEBUG')
    # 定义输出格式
    fmt = "%(asctime)s - %(name)s -[%(filename)s:%(lineno)s]- %(levelname)s - [%(message)s] "
    formate = logging.Formatter(fmt)

    # 输出日志文件的路径，绝对路径
    file_name = os.path.join(c02_contants.logs_dir, 'case.log')
    # 输出到文件
    file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=20*1024*1024, backupCount=10,encoding='utf-8')
    level = config.get('log','file_handler')
    # 设置输出指定文件日志的级别，输出由handle决定，以及输出到那里，输出到文件
    file_handler.setLevel(level)
    # 输出到文件的格式
    file_handler.setFormatter(formate)

    # 输出到控制台
    console_handler = logging.StreamHandler()
    level = config.get('log','console_handler')
    console_handler.setLevel(level)
    console_handler.setFormatter(formate)

    # 将日志收集器和输出渠道对接，添加handler时候里边本就有，所以不会重复输出两条日志，不需要移除重复日志
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

if __name__ == '__main__':

    logger = get_logger(logger_name='invest')
    logger.error('this is error message eeeeee')
    logger.info('this is info message iiiiii')
    logger.debug('this is info message dddddd')

