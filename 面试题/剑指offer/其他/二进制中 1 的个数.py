
"""
输入一个整数，输出该数二进制表示中 1 的个数。
"""
class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n is not 0:
            count += 1
            n = n & (n - 1)
        return count