"""
题目描述
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
"""

# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        nums = [0] * (number + 1)
        nums[0] = 0
        nums[1] = 1
        nums[2] = 2
        nums[3] = 3
        for index in range(4, number + 1):
            max = 0
            for i in range(1, index//2 + 1):
                temp = nums[i] * nums[index - i]
                if temp > max:
                    max = temp
            nums[index] = max
        return nums[number]

solution = Solution()
num = solution.cutRope(4)
print(num)
