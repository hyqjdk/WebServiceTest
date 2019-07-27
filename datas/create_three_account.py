# -*- coding: utf-8 -*-
# 生成3个账号
# @Time    : 2019/7/14 23:22
# @Author  : YoYo
from scripts.handle_mobilephone import MobilePhoneUtils
from scripts.handle_request import CommonRequests

request = CommonRequests()
url = 'http://tj.lemonban.com/futureloan/mvc/api/member/register'

# 注册借款人账号
# common_account = MobilePhoneUtils.create_not_exist_mobile()
common_param = '{"mobilephone":"13501265379","pwd":"123456","regname":"commpn_yoyo"}'
common_response = request.request("POST", url, common_param)
print(str(common_response.json()))

# 注册投资人账号
# invest_account = MobilePhoneUtils.create_not_exist_mobile()
# common_param = '{"mobilephone":"13163275081","pwd":"123456","regname":"commpn_yoyo"}'
# common_response = request.request("POST", url, common_param)
# print(common_response)
#
# # 注册管理人账号
# manager = MobilePhoneUtils.create_not_exist_mobile()
# print(manager)

# 15835718462
# 13163275081
# 13501265379

