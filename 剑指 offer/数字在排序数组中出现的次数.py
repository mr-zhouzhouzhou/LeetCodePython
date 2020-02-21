"""
题目描述
统计一个数字在排序数组中出现的次数。
"""

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if k not in data:
            return 0
        nums = 0
        for item in data:
            if item<k:
                continue
            elif item == k:
                nums = nums + 1
            else:
                return nums
        return nums