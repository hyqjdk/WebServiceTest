# -*- coding: utf-8 -*-
# 参数化处理
# @Time    : 2019/7/14 10:26
# @Author  : YoYo

import re

from scripts.constant_url import ACCOUNTS_PATH
from scripts.handle_config import ConfigLoader
from scripts.handle_idcard import IdCardUtils


class Context:
    """获取测试数据参数化类"""
    # 获取验证码
    code_db_id = r'\$\{db_id\}'  # 哪个数据库下
    code_table_id = r'\$\{table_id\}'  # 哪个table下的
    register_phone = r'\$\{register_phone\}'

    # 验证码
    verify_code_pattern = r'\$\{verify_code\}'
    # 身份证
    id_card_pattern = r'\${\cre_id\}'
    # uid
    user_id_pattern = r'\$\{user_id\}'

    @classmethod
    def verify_code_replace(cls, pattern_data):
        """
         替换验证码
        :param pattern_data: 传入的所有数据
        :return:
        """
        if re.search(cls.verify_code_pattern, pattern_data) and hasattr(Context, "verify_code"):
            code = getattr(Context, "verify_code")
            pattern_data = re.sub(cls.verify_code_pattern, str(code), pattern_data)
        return pattern_data

    @classmethod
    def id_card_replace(cls, pattern_data):
        """
         替换验证码
        :param pattern_data: 传入的所有数据
        :return:
        """
        if re.search(cls.id_card_pattern, pattern_data):
            card_id = IdCardUtils.get_random_id_card()
            pattern_data = re.sub(cls.id_card_pattern, str(card_id), pattern_data)
        return pattern_data

    @classmethod
    def user_id_replace(cls, pattern_data):
        """
         替换验证码
        :param pattern_data: 传入的所有数据
        :return:
        """
        if re.search(cls.user_id_pattern, pattern_data) and hasattr(Context, "f_uid"):
            id = getattr(Context, "f_uid")
            pattern_data = re.sub(cls.user_id_pattern, str(id), pattern_data)
        return pattern_data

    @classmethod
    def sendMCode_parameterization(cls, data):
        """
        替换
        :param data: 原始数据
        :return:
        """
        if re.search(cls.register_phone, data):
            config = ConfigLoader()
            mobile_phone = config.get_value("account", "register_account")
            data = re.sub(cls.register_phone, mobile_phone, data)
        return data

    @classmethod
    def register_parameterization(cls, data):
        """
        注册部分参数化
        :param data: 原始数据 select Fverify_code from sms_db_${db_id}.t_mvcode_info_${table_id} WHERE Fmobile_no = ${register_phone}
        :return:
        """
        config = ConfigLoader(ACCOUNTS_PATH)
        mobile_phone = config.get_value("account", "register_account")
        setattr(Context, "db_name", "sms_db_" + mobile_phone[-2:])
        if re.search(cls.register_phone, data):
            data = re.sub(cls.register_phone, mobile_phone, data)
        if re.search(cls.code_db_id, data):
            data = re.sub(cls.code_db_id, mobile_phone[-2:], data)
        if re.search(cls.code_table_id, data):
            data = re.sub(cls.code_table_id, mobile_phone[-3], data)
        data = cls.verify_code_replace(data)
        return data

    @classmethod
    def verifyUserAuth_parameterization(cls, data):
        """
        实名认证参数化
        :param data: 原始数据
        :return:
        """
        data = cls.user_id_replace(data)
        data = cls.id_card_replace(data)
        return data

# if __name__ == '__main__':
# setattr(Context, "verify_code", str("11456"))
# data = '{"verify_code": "${verify_code}", "user_id": "yoyo", "channel_id": "1", "pwd": "123456", "mobile": "15900743992","ip": "129.45.6.7"}'
# new_data = Context.verify_code_replace(data)
# print(new_data)
