"""

给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n）
，每段绳子的长度记为k[1],...,k[m]。请问k[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
"""



# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        if number <= 1:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        temp = [0] * (number + 1)
        temp[1] = 1
        temp[2] = 2
        temp[3] = 3
        for index in range(4, number + 1):
            max_result = 0
            for val in range(1, index//2 + 1):
                if max_result < temp[val] * temp[index-val]:
                    max_result = temp[val] * temp[index-val]
            temp[index] = max_result
        return temp


solution = Solution()


print(solution.cutRope(15))