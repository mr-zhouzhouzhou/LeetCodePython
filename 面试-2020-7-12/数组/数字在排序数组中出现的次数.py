"""
题目描述
统计一个数字在排序数组中出现的次数。
"""


class Solution:
    def GetNumberOfK(self, data, k):
        start = 0
        end = len(data) -1
        if len(data) == 1:
            if data[0] == k:
                return 1
            else:
                return 0
        while start < end:
            if data[start] < k:
                start +=1
            if data[end] > k:
                end -= 1
            if data[start] == k and data[end] == k:
                return end - start + 1
        return 0
