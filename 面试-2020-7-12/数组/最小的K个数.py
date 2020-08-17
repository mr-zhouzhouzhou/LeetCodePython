"""
题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k <= 0 or k >len(tinput):
            return []
        self.quick_sort(tinput, 0, len(tinput)-1)
        return tinput[:k]

    def quick_sort(self, arr, low, high):
        if low < high:
            q = self.partition(arr, low, high)
            self.quick_sort(arr, low, q - 1)
            self.quick_sort(arr, q + 1, high)
        return arr

    def partition(self, arr, low, high):
        pix = arr[high]
        i = low - 1
        for index in range(low, high):
            if arr[index] <= pix:
                i = i + 1
                arr[i], arr[index] = arr[index], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]

        return i + 1




array = [4,5,1,4,3,7,3,5]
k = 8
solution = Solution()

print(solution.quick_sort(array, 0, 7))

