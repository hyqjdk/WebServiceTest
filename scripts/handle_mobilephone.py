# -*- coding: utf-8 -*-
# 处理手机号类
# @Time    : 2019/7/12 17:27
# @Author  : YoYo
import random
from scripts.handle_mysql import HandleMySql
from scripts.base_account_data import Accounts


class MobilePhoneUtils:
    """手机号工具类"""

    @staticmethod
    def get_random_phone():
        """随机生成手机号"""
        first_list = ["130", "131", "132", "133", "134", "135", "138", "139", "150", "151", "152", "154", "156",
                      "157", "158", "159", "187", "188", "189"]
        number_first_part = random.choice(first_list)
        number_second_part = random.sample("0123456789", 8)  # 后八位取随机数
        second = "".join(number_second_part)
        return number_first_part + second

    @staticmethod
    def is_phone_exist(current_phone):
        """判断手机号是否存在"""
        handle_sql = HandleMySql()
        sql = "select MobilePhone from future.member where MobilePhone = %s;"
        my_dict = handle_sql.get_value(sql, (current_phone,))
        handle_sql.close()
        if my_dict is None:
            return False
        else:
            return True

    @staticmethod
    def create_not_exist_mobile():
        """获取未生成的手机号"""
        while True:
            random_mobile = MobilePhoneUtils.get_random_phone()
            if not MobilePhoneUtils.is_phone_exist(random_mobile):
                break
        return random_mobile

    @staticmethod
    def create_exist_mobile():
        """获取已经生成的手机号"""
        handle_sql = HandleMySql()
        sql = "select MobilePhone from member limit 0,1;"
        my_dict = handle_sql.get_value(sql)
        handle_sql.close()
        return my_dict["MobilePhone"]

    @staticmethod
    def get_common_mobile():
        """获取已经生成的手机号"""
        return Accounts.admin_user

if __name__ == '__main__':
    phone = MobilePhoneUtils.get_common_mobile()
    print(phone)
    # is_phone_exist = MobilePhoneUtils.create_exist_mobile()
    # print(is_phone_exist)
