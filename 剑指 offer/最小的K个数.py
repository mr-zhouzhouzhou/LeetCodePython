"""
题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""
"""


思路： 快速排序变型

"""
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k == 0:
            return []
        if k >= len(tinput):
            if k > len(tinput):
                return []
            else:
                tinput.sort()
                return tinput
        index = -1
        start = -1
        end = len(tinput)-1
        while index != k:
            if index < k:
                start = start + 1
                index = self.pai(tinput, start, end)
            elif index > k:
                end = index - 1
                index = self.pai(tinput, start, end)
        temp = tinput[:k]
        temp.sort()
        return temp

    def pai(self, tinput, start, end):
        flag = tinput[start]
        while start < end:
            while tinput[end] >= flag and start < end:
                end = end - 1
            tinput[start] = tinput[end]
            while tinput[start] <= flag and start < end:
                start = start + 1
            tinput[end] = tinput[start]
        tinput[end] = flag
        return start



solution = Solution()

nums,n = [4,7,2,3,8,1,9,5,6], 8
#nums, n= [4,5,1,6,2,7,3,8],8
print(solution.GetLeastNumbers_Solution(nums,n))
# nums = [4,7,2,3,8,1,9,5,6]
# nums.sort()
# print(nums)