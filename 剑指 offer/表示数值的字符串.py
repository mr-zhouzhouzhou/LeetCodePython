"""
题目描述
请实现一个函数用来判断字符串是否表示数值（包括整数和小数)。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""


# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        pass

from io import  StringIO

s = StringIO()


m_dict = {"1":21}
s.write(str(m_dict))

a = s.getvalue()
s.close()
