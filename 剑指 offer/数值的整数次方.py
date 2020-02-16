"""
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0
"""


# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0 and exponent <= 0:  # 考虑边界，当base为0并且指数小于0，便没有意义
            return 0
        absexponent = abs(exponent)  # 求绝对值
        result = self.PowerDeal(base, absexponent)  # 只求正数的指数
        if exponent == 0:  # 如果指数为0，则结果为1
            return 1
        elif exponent < 0:  # 如果指数为负数，则结果是正数的倒数
            result = 1 / result
        return result

    def PowerDeal(self, base, exponent):  # 采用循环的思路是O(n)
        result = 1.0
        for i in range(exponent):
            result *= base
        return result