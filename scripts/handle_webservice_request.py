# -*- coding: utf-8 -*-
# 封装请求类
# @Time    : 2019/7/7 9:26
# @Author  : YoYo
import suds
from requests import HTTPError
from suds.client import Client,WebFault


class WebServiceRequests:
    def __init__(self):
        self.client = None

    def request(self, url, method_name, data):
        """
        WebService请求
        :param url: 地址
        :param method_name: 接口名称
        :param data: 数据
        :return: is_success:是否请求成功，返回值
        """
        is_success = False
        self.client = Client(url)
        try:
            result = self.client.service.__getattr__(method_name)(data)
            is_success = True
            return is_success, result
        except WebFault as ex:  # 返回错误
            return is_success, ex

    def get_all_methods(self):
        """
        获取一个地址内的所有的接口
        :return:
        """
        return [method for method in self.client.wsdl.services[0].ports[0].methods]
