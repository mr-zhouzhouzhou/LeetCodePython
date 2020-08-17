"""

题目描述
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。
 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
 但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

"""

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        nums = [0]
        mark = [[False for _ in range(cols)] for _ in range(rows)]

        self.soultion(threshold, rows - 1, cols - 1, 0, 0, nums, mark)
        return nums[0]

    def soultion(self, threshold, rows, cols, x, y, nums, mark):
        #print(threshold, rows, cols, x, y, nums, mark)
        if x < 0 or y < 0 or x > rows or y > cols:
            return
        temp = 0
        for item in str(x):
            temp = temp + int(item)
        for item in str(y):
            temp = temp + int(item)
        if temp > threshold or mark[x][y] is True:
            return
        mark[x][y] = True
        nums[0] += 1
        self.soultion(threshold, rows, cols, x - 1, y, nums, mark)
        self.soultion(threshold, rows, cols, x + 1, y, nums, mark)
        self.soultion(threshold, rows, cols, x, y - 1, nums, mark)
        self.soultion(threshold, rows, cols, x, y + 1, nums, mark)



solution = Solution()
print(solution.movingCount(4, 10, 10))