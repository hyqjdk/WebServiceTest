# -*- coding: utf-8 -*-
# 演练正则表达
# @Time    : 2019/7/14 23:46
# @Author  : YoYo
import re

s = '{"mobilephone":"${register}","pwd":"123456"}'
mobilephone = "13800000000"  # 正则表达式
s = s.replace(mobilephone, "13800000001")
print(s)
res4 = re.findall(pattern='\$\{(.*?)\}', string=s)
print(res4)
res5 = re.sub(pattern='\$\{(.*?)\}', repl="123456", string=s)
print(res5)

s1 = "www.lemonban.com"
p = "(w)(ww)"  # () 进行分组
m = re.search(p, s1)
print(m)
print(m.group(0))  # 全匹配
print(m.group(1))  # 取到第一个分组里面的字符
print(m.group(2))  # 取到第二个分组里面的字符
