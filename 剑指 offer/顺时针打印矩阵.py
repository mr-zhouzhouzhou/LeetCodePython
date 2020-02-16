"""

题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1, 2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""
"""

思路：
1：把矩阵拆成两个部分 1：循环 2：每次只遍历一圈
"""

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        row_len = len(matrix)
        col_len = len(matrix[0])
        n = min((row_len-1)//2, (col_len-1)//2)
        nums = []
        for item in range(n + 1):
            self.printMatrixByindex(item, matrix, nums)
        return nums


    def printMatrixByindex(self, k, matrix, nums):
        row_len = len(matrix[0])
        col_len = len(matrix)
        temp = k
        while temp < row_len - k:
            nums.append(matrix[k][temp])
            temp = temp + 1
        temp1 = temp - 1
        temp = k + 1

        while temp < col_len - k:
            nums.append(matrix[temp][temp1])
            temp = temp + 1
        temp2 = temp - 1
        temp = temp1 - 1
        if row_len - k <= 1 or col_len - k <= 1:
            return
        while temp >= k and temp2 > k:
            nums.append(matrix[temp2][temp])
            temp = temp - 1

        temp = temp2 - 1
        while temp > k:
            nums.append(matrix[temp][k])
            temp = temp - 1





matrix = [[1,   2,  3, 4],
          [12, 13, 14, 5],
          [11, 16, 15, 6],
          [10,  9,  8, 7]]
#matrix = [[1],[2],[3],[4],[5]]
matrix = [[1,2,3,4,5]]
solution = Solution()
print(solution.printMatrix(matrix))