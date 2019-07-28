# -*- coding: utf-8 -*-
# 参数化处理
# @Time    : 2019/7/14 10:26
# @Author  : YoYo

import re

from scripts.handle_mobilephone import MobilePhoneUtils
from scripts.base_account_data import Accounts


class Context:
    """获取测试数据参数化类"""
    # 获取验证码
    code_db_id = r'\$\{db_id\}' # 哪个数据库下
    code_table_id = r'\$\{table_id\}' # 哪个table下的
    register_phone = r'\$\{register_phone\}'

    # 验证码
    verify_code = r'\$\{verify_code\}'
    #select Fverify_code from sms_db_${db_id}.t_mvcode_info_${table_id} WHERE Fmobile_no = ${register_phone}

    @classmethod
    def verify_code_replace(cls, pattern_data):
        """
         替换验证码
        :param pattern_data: 传入的所有数据
        :return:
        """
        if re.search(cls.verify_code, pattern_data):
            verify_code = getattr(Context, "verify_code")
            pattern_data = re.sub(cls.verify_code, verify_code, pattern_data)
        return pattern_data

    @classmethod
    def sendMCode_parameterization(cls, mobile_phone, data):
        """
        替换
        :param mobile_phone: 手机号
        :param data: 原始数据
        :return:
        """
        if re.search(cls.code_db_id, data):
            data = re.sub(cls.code_db_id, mobile_phone., data)
        if re.search(cls.invest_user_pwd, data):
            invest_pwd = Accounts.invest_pwd
            data = re.sub(cls.invest_user_pwd, invest_pwd, data)
        return data
        return data

    @classmethod
    def register_parameterization(cls, data):
        """
        注册部分参数化
        :param data: 原始数据
        :return:
        """
        data = cls.verify_code_replace(data)
        data = cls.exist_tel_replace(data)
        return data
































    @classmethod
    def not_exist_tel_replace(cls, data):
        """
        替换成需要的数据显示类型
        :param data: 原始数据
        :return:
        """
        if re.search(cls.not_exist_tel_pattern, data):
            not_exist_tel = MobilePhoneUtils.create_not_exist_mobile()
            data = re.sub(cls.not_exist_tel_pattern, not_exist_tel, data)
        return data

    @classmethod
    def exist_tel_replace(cls, data):
        """
        替换成需要的数据显示类型
        :param data: 原始数据
        :return:
        """
        if re.search(cls.exist_tel_pattern, data):
            exist_tel = MobilePhoneUtils.create_exist_mobile()
            data = re.sub(cls.exist_tel_pattern, exist_tel, data)
        return data

    @classmethod
    def exist_member_id_replace(cls, member_id, data):
        """
        替换成需要的数据显示类型
        :param data: 原始数据
        :return:
        """
        if re.search(cls.exist_tel_pattern, data):
            data = re.sub(cls.exist_id_pattern, member_id, data)
        return data

    @classmethod
    def common_tel_replace(cls, data):
        """
        替换成普通用户的账户
        :param data: 原始数据
        :return:
        """
        if re.search(cls.exist_tel_pattern, data):
            exist_tel = MobilePhoneUtils.get_common_mobile()
            data = re.sub(cls.exist_tel_pattern, exist_tel, data)
        return data

    @classmethod
    def invest_tel_replace(cls, data):
        """
        替换成“投资人”的账户
        :param data: 原始数据
        :return:
        """
        if re.search(cls.exist_tel_pattern, data):
            exist_tel = Accounts.invest_user
            data = re.sub(cls.exist_tel_pattern, exist_tel, data)
        return data

    @classmethod
    def normal_tel_replace(cls, data):
        """
        替换成“投资人”的账户
        :param data: 原始数据
        :return:
        """
        if re.search(cls.exist_tel_pattern, data):
            exist_tel = Accounts.normal_user
            data = re.sub(cls.exist_tel_pattern, exist_tel, data)
        return data

    @classmethod
    def loan_id_replace(cls, data):
        """
        替换成“投资人”的账户
        :param data: 原始数据
        :return:
        """
        if re.search(cls.loan_id, data):
            # loan_id = getattr(Context, "loan_id")
            loan_id = Context.loan_id
            data = re.sub(cls.loan_id, loan_id, data)
        return data

    @classmethod
    def admin_tel_replace(cls, data):
        """
        替换成“管理员”的账户
        :param data: 原始数据
        :return:
        """
        if re.search(cls.admin_user_tel, data):
            admin_id = Accounts.admin_user
            data = re.sub(cls.admin_user_tel, admin_id, data)
        return data

    @classmethod
    def borrow_tel_replace(cls, data):
        """
        替换成“借款人”的账户
        :param data: 原始数据
        :return:
        """
        if re.search(cls.borrow_user_tel, data):
            borrow_user_tel = Accounts.normal_id
            data = re.sub(cls.borrow_user_tel, borrow_user_tel, data)
        return data

    @classmethod
    def invest_replace(cls, data):
        """
        替换成“借款人”的账户
        :param data: 原始数据
        :return:
        """
        if re.search(cls.invest_user_id, data):
            invest_user = Accounts.invest_user
            data = re.sub(cls.invest_user_id, invest_user, data)
        if re.search(cls.invest_user_pwd, data):
            invest_pwd = Accounts.invest_pwd
            data = re.sub(cls.invest_user_pwd, invest_pwd, data)
        return data

    @classmethod
    def register_parameterization(cls, data):
        """
        注册部分参数化
        :param data: 原始数据
        :return:
        """
        data = cls.not_exist_tel_replace(data)
        data = cls.exist_tel_replace(data)
        return data

    @classmethod
    def login_parameterization(cls, data):
        """
        登陆部分参数化
        :param data: 原始数据
        :return:
        """
        data = cls.exist_tel_replace(data)
        return data

    @classmethod
    def recharge_parameterization(cls, data):
        """
        充值部分参数化
        :param data: 原始数据
        :return:
        """
        data = cls.common_tel_replace(data)
        return data

    @classmethod
    def recharge_parameterization(cls, member_id, data):
        """
        充值部分参数化
        :param data: 原始数据
        :return:
        """
        data = cls.normal_tel_replace(data)
        data = cls.exist_member_id_replace(member_id, data)
        return data

    @classmethod
    def add_parameterization(cls, member_id, data):
        """
        借款部分参数化
        :param data: 原始数据
        :return:
        """
        data = cls.normal_tel_replace(data)
        data = cls.exist_member_id_replace(member_id, data)
        return data

    @classmethod
    def invest_parameterization(cls, data):
        """
        投资、竞标部分参数化
        :param data: 原始数据
        :return:
        """
        data = cls.admin_tel_replace(data)
        data = cls.borrow_tel_replace(data)
        data = cls.loan_id_replace(data)
        data = cls.invest_replace(data)
        return data


if __name__ == '__main__':
    data = '{"mobilephone":"${not_exist_tel}","password":"123456","regname":"yoyo"}'
    print(Context.register_parameterization(data))
