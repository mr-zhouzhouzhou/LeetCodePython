"""


题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        temp = [0] * len(array)
        low = 0
        for index, item in enumerate(array):
            if item % 2 == 1:
                temp[low] = item
                low += 1

        high = len(array) - 1


        for index in range( len(array) - 1, -1 , -1):
            if array[index] % 2 == 0:
                temp[high] = array[index]
                high -= 1
        return temp



for item in range(10,6, -1):
    print(item)
