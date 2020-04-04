"""
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
"""

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        length = len(array)
        if length < 2:
            return []
        temp = []
        min = 9999999999
        length = len(array)
        for m in range(length - 1):
            for n in range(m + 1, length):
                if array[m] + array[n] == tsum:
                    if min > array[m] * array[n]:
                        temp = []
                        temp.append(array[m])
                        temp.append(array[n])
                        min = array[m] * array[n]
        return temp

solution = Solution()

array = [0, 1,2,3,4,5,6,7,8,9]
tsum = 9
temp = solution.FindNumbersWithSum(array, tsum)


