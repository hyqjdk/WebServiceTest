# -*- coding: utf-8 -*-
# 
# @Time    : 2019/7/26 16:21
# @Author  : YoYo
from scripts.handle_webservice_request import WebServiceRequests as Request

# url = "http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
# t = {"client_ip": "129.45.6.7", "tmpl_id": "1", "mobile": ""}  # 用字典的方式传值
# request = Request()
# is_sucess, result = request.request(url, "sendMCode", t)
# print(result.fault.faultcode)
# print(result.fault.faultstring)

url = "http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
t = {"verify_code": "1234", "user_id": "yoyo", "channel_id": "1", "pwd": "123456", "mobile": "15900743991",
     "ip": "129.45.6.7"}  # 用字典的方式传值
request = Request()
is_sucess, result = request.request(url, "userRegister", t)
print(result)
# print(result.fault.faultstring)
