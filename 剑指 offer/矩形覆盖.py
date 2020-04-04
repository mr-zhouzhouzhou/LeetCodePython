"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number < 1:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        if number == 3:
            return 3
        nums = [0] * (number + 1)
        nums[0] = 0
        nums[1] = 2
        nums[2] = 2
        nums[3] = 3
        for index in range(4, number + 1):
            nums[index] = nums[index - 1] + nums[index - 2]
        return nums[number]







