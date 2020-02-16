"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
import math
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        c = 0
        if n<0:
            n = n&0xffffffffffffffffff
        while n:
            c += 1
            n &= n-1
        return c



solution = Solution()
print(solution.NumberOf1(-1))

a=10
a &= a-1

print(a)
print((-1&0xff)&(-1&0xff))