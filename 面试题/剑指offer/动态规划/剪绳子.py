"""
剪绳子：把一根绳子剪成多段，并且使得每段的长度乘积最大。
"""

"""
1: 一个数字，可以拆成2个部分去取最大值
2
动态规划，把一个问题小问题拼接成一个大问题
"""

class Solution:
    def cutRope(self, number):

        dp = [0] * (number + 1)
        for i in range(2, number + 1):
            for j in range(1, i//2 + 1):
                dp[i] = max(j * (i-j), dp[j] * dp[i - j])
        return dp[number]




soultion = Solution()
print(soultion.cutRope(10))
print(soultion.cutRope(1))
print(soultion.cutRope(2))



