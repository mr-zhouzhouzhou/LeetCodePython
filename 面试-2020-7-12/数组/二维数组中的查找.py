"""

题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array)
        cols = len(array[0])

        row = rows - 1
        col = 0
        while col < cols and row >= 0:
            print(array[row][col])
            if array[row][col] > target:
                row -= 1
            elif  array[row][col] < target:
                col += 1
            else:
                return True
        return False



array=[[1,2,8,9],
       [2,4,9,12],
       [4,7,10,13],
       [6,8,11,15]]
target = 1
solution = Solution()


print(solution.Find(target, array))