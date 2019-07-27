# -*- coding: utf-8 -*-
# 配置文件封装
# @Time    : 2019/6/29 16:25
# @Author  : YoYo
from configparser import ConfigParser
from scripts.constant_url import CONFIG_FILE_PATH


class ConfigLoader:
    def __init__(self, file_name=None):
        self.file_name = file_name
        self.config = ConfigParser()
        if self.file_name is None:
            """获取默认路径下的配置文件"""
            self.config.read(CONFIG_FILE_PATH, encoding="utf-8")
        else:
            """获取指定路径下的配置文件"""
            self.config.read(self.file_name, encoding="utf-8")

    def get_value(self, section, option):
        # 通过section，option 来取到配置项的值
        return self.config.get(section, option)

    def get_boolean(self, section, option):
        return self.config.getboolean(section, option)

    def get_int(self, section, option):
        return self.config.getint(section, option)

    def get_float(self, section, option):
        return self.config.getfloat(section, option)

    def get_eval_data(self, section, option):
        """
        获取列表形式的配置值
        :param section:
        :param option:
        :return:
        """
        return eval(self.get_value(section, option))

    @staticmethod
    def write_config_data(config_data, file_name):
        """
        保存传入的内容为字典的列表类型的配置数据
        :param config_data: 容为字典的列表类型的配置数据
        :param file_name: 文件名
        """
        config = ConfigParser()
        for key in config_data:
            config[key] = config_data[key]
        with open(file_name, "w") as file:
            config.write(file)
