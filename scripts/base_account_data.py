# -*- coding: utf-8 -*-
# 所需的基础账户数据
# @Time    : 2019/7/13 10:51
# @Author  : YoYo
from scripts.handle_config import ConfigLoader
from scripts.constant_url import ACCOUNTS_PATH


class Accounts:
    """测试基础账号"""
    config = ConfigLoader(ACCOUNTS_PATH)
    normal_user = config.get_value("accounts", "normal_user")
    normal_pwd = config.get_value("accounts", "normal_pwd")
    normal_id = config.get_value("accounts", "normal_id")

    # 管理员账号
    admin_user = config.get_value("accounts", "admin_user")
    admin_pwd = config.get_value("accounts", "admin_pwd")
    admin_id = config.get_value("accounts", "admin_id")

    # 投资人账号
    invest_user = config.get_value("accounts", "invest_user")
    invest_pwd = config.get_value("accounts", "invest_pwd")
    invest_id = config.get_value("accounts", "invest_id")

    base_url = config.get_value("url", "base_url")
