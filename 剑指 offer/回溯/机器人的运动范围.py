"""
题目描述
地上有一个m行和n列的方格。
一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），
因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        count = [0]
        visited = [[ False for _ in range(cols)] for _ in range(rows)]
        self.soultion(threshold, rows, cols, 0, 0, count, visited)
        return count[0]

    def soultion(self, threshold, rows, cols, i, j, count, visited):
        if i >= rows or j >= cols or i < 0 or j < 0:
            return False
        if self.getSum(i, j) > threshold or visited[i][j]:
            return False
        visited[i][j] = True
        count[0] = count[0] + 1
        self.soultion(threshold, rows, cols, i - 1, j, count, visited) or \
        self.soultion(threshold, rows, cols, i + 1, j, count, visited) or \
        self.soultion(threshold, rows, cols, i, j + 1, count, visited) or \
        self.soultion(threshold, rows, cols, i, j - 1, count, visited)

    def getSum(self, num1, num2):
        count = 0
        for item in str(num1):
            count = count + int(item)
        for item in str(num2):
            count = count + int(item)
        return count


solution = Solution()
count = solution.movingCount(5, 5, 6)
#
print(count)





