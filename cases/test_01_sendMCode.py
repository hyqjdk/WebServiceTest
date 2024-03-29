# -*- coding: utf-8 -*-
# 发送验证码接口
# @Time    : 2019/7/26 11:11
# @Author  : YoYo

import os
import unittest

from libs.ddt import ddt, data
from scripts.constant_url import DATA_FILE_PATH, RESULT_EXCEL_FILE_PATH
from scripts.handle_excel import HandleExcel
from scripts.handle_log import Logging
from scripts.handle_webservice_request import WebServiceRequests
from suds.client import WebFault

# 获取用例数据列表
handle_excel = HandleExcel()
excel = handle_excel.get_exist_excel(DATA_FILE_PATH)
cases = handle_excel.get_cases("send_msg")


@ddt
class TestSendMCode(unittest.TestCase):
    """发送验证码接口测试"""

    @classmethod
    def setUpClass(cls):
        cls.request = WebServiceRequests()
        cls.my_excel = HandleExcel()
        cls.my_excel.get_exist_excel(os.path.join(RESULT_EXCEL_FILE_PATH, "my_result.xlsx"))
        cls.case_list = []

    @classmethod
    def tearDownClass(cls):
        cls.my_excel.save_list_data("send_msg", cls.case_list)

    @data(*cases)
    def test_sendMCode(self, case):
        print(case)
        Logging.info("测试用例名称为：{}".format(case["title"]))
        is_success, response = TestSendMCode.request.request(case["url"], case["method_name"], eval(case["data"]))
        if is_success:
            case["actual"] = response["retCode"]
            case["result"] = str(response)
            TestSendMCode.case_list.append(case)
            Logging.info("response：{}".format(str(response)))
            try:
                self.assertEqual(int(case["expected"]), int(response["retCode"]))
            except AssertionError as e:
                Logging.info("具体异常为：{}".format(e))
                raise e
        else:
            if isinstance(response, WebFault):
                case["actual"] = response.fault.faultcode  # 错误代码
                case["result"] = response.fault.faultstring  # 错误描述
                TestSendMCode.case_list.append(case)
                Logging.info("response：{}".format(str(response.fault)))
                try:
                    self.assertEqual(str(case["expected"]), response.fault.faultcode)
                except AssertionError as e:
                    Logging.info("具体异常为：{}".format(e))
                    raise e
