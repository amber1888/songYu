import logging
import os
from functools import lru_cache
from logging.handlers import RotatingFileHandler

log_dir_path = './log/'
if not os.path.isdir(log_dir_path):
    os.makedirs(log_dir_path)

logger = logging.getLogger()
# 设置logger可输出日志级别范围
logger.setLevel(logging.INFO)


@lru_cache()
def log_init():
    # 添加控制台handler，用于输出日志到控制台
    console_handler = logging.StreamHandler()
    # 添加日志文件handler，用于输出日志到文件中
    file_handler = RotatingFileHandler(filename=log_dir_path + 'songYu.log',
                                       maxBytes=50 * 1024 * 1024,
                                       backupCount=9,
                                       encoding='UTF-8')

    # 设置格式并赋予handler
    formatter = logging.Formatter(
        '[%(asctime)s] -- %(levelname)s - [%(thread)d][%(threadName)s] -- %(filename)s[line:%(lineno)d]: %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 将handler添加到日志器中
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.info("日志组件加载成功")
