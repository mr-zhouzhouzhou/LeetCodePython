"""
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""

"""
思路：
这题优化点 在于用2个数字去记录前面两个数字

"""

class Solution:
    def Fibonacci(self, n):
        first, second = 1, 1
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        n = n - 2
        fib_num = 0
        for index in range(n):
            fib_num = first + second
            first, second = second, fib_num
        return fib_num



solution = Solution()

print(solution.Fibonacci(13))
