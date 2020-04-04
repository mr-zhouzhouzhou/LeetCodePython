"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""


# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 0:
            return 0
        if number <= 2:
            return 1 if number == 1 else 2
        all_jump = 3
        number = number - 2
        jumps = 0
        for index in range(number):
            jumps = all_jump + 1
            all_jump = all_jump + jumps
        return jumps