# -*- coding: utf-8 -*-
# 自动化接口测试主入口
# @Time    : 2019/5/4 22:16
# @Author  : YoYo

import unittest
from scripts.constant_url import CASES_PATH, REPORT_PATH
from libs import HTMLTestRunnerNew
import datetime
import os

discover = unittest.defaultTestLoader.discover(CASES_PATH, pattern='test*.py', top_level_dir=None)

# 报告完整地址
# 报告名称加时间戳
name = "test_report_" + datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S") + ".html"
url = os.path.join(REPORT_PATH, name)
with open(url, "wb") as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(f, title=u'测试报告', description=u'用例执行情况：', tester="YoYo")
    runner.run(discover)
