# -*- coding: utf-8 -*-
# 对于日志处理的封装
# @Time    : 2019/6/29 17:43
# @Author  : YoYo

import logging
from scripts.handle_config import ConfigLoader
from scripts.constant_url import LOG_PATH
import datetime
import os


class Logging:

    def __init__(self):
        config = ConfigLoader()
        # 1.定义日志收集器
        self.case_logger = logging.getLogger(config.get_value("logging", "logger_name"))
        self.case_logger.setLevel(config.get_value("logging", "logger_level"))  # 定义收集器的等级

        # 设置控制台输出
        console_handler = logging.StreamHandler()  # "控制台"输出渠道
        console_handler.setLevel(config.get_value("logging", "console_level"))  # 设置等级
        simple_formatter = logging.Formatter(config.get_value("logging", "simple_formatter"))
        console_handler.setFormatter(simple_formatter)  # 设置日志显示格式

        # 设置文件输出
        name = "my_loging_" + datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S") + ".log"
        file_handler = logging.FileHandler(os.path.join(LOG_PATH, name), encoding="utf-8")
        file_handler.setLevel(config.get_value("logging", "file_level"))
        file_formatter = logging.Formatter(config.get_value("logging", "file_formatter"))
        file_handler.setFormatter(file_formatter)

        # 将日志收集器与输出渠道进行对接
        self.case_logger.addHandler(console_handler)
        self.case_logger.addHandler(file_handler)

    def info(self, msg):
        self.case_logger.info(msg)

    def debug(self, msg):
        self.case_logger.debug(msg)

    def warning(self, msg):
        self.case_logger.warning(msg)

    def error(self, msg):
        self.case_logger.error(msg)

    def critical(self, msg):
        self.case_logger.critical(msg)


# 创建一个logging对象
Logging = Logging()

# if __name__ == "__main__":
#     logging = Logging()
#     logging.error("测试一下下")
