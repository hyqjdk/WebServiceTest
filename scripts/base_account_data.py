# -*- coding: utf-8 -*-
# 所需的基础账户数据
# @Time    : 2019/7/13 10:51
# @Author  : YoYo
from scripts.handle_config import ConfigLoader
from scripts.constant_url import ACCOUNTS_PATH


class Accounts:
    """测试基础账号"""
    config = ConfigLoader(ACCOUNTS_PATH)
    register_phone = config.get_value("account", "register_account")
