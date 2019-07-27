# -*- coding: utf-8 -*-
# 常用地址
# @Time    : 2019/7/12 16:27
# @Author  : YoYo

import os

# 获取项目根目录
# one_path = os.path.abspath(__file__)
# two_path = os.path.dirname(one_path)
# three_path = os.path.dirname(two_path)
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试用例地址
CASES_PATH = os.path.join(BASE_PATH, "cases")

# 获取测试数据所在目录的绝对地址
DATA_PATH = os.path.join(BASE_PATH, "datas")
# 获取测试数据文件的地址
DATA_FILE_PATH = os.path.join(DATA_PATH, "cases.xlsx")

# 获取配置文件configs所在的目录的路径
CONFIG_PATH = os.path.join(BASE_PATH, "configs")
CONFIG_FILE_PATH = os.path.join(CONFIG_PATH, "configure.conf")
# 测试账号的配置地址
ACCOUNTS_PATH = os.path.join(CONFIG_PATH, "accounts.conf")

# 获取报告的地址
REPORT_PATH = os.path.join(os.path.join(BASE_PATH, "outputs"), "reports")

# 获取loging地址
LOG_PATH = os.path.join(os.path.join(BASE_PATH, "outputs"), "logs")

# 结果excel的地址
RESULT_EXCEL_FILE_PATH = os.path.join(os.path.join(BASE_PATH, "outputs"), "result_excels")
