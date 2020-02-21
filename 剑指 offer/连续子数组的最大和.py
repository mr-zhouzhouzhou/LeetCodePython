"""
题目描述
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:
在古老的一维模式识别中,常常需要计算连续子向量的最大和,
当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
"""

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        pre = 0
        max_num = -9999999999
        for item in array:
            if pre + item >= item:
                pre = pre + item
            else:
                pre = item
            if pre > max_num:
                max_num = pre

        return max_num


array = [1,-2,3,10,-4,7,2,-5]
solution = Solution()

print(solution.FindGreatestSumOfSubArray(array))
