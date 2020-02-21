"""
题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
"""


# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        item_dict = {}
        for item in numbers:
            if item in item_dict.keys():
                duplication[0] = item
                return True
            else:
                item_dict[item] = 1
        return False
solution = Solution()
nums = [2,1,3,1,4]
duplication = []
print(solution.duplicate(nums, duplication))