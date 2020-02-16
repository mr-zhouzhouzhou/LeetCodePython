"""
题目描述
数组中有一个数字出现的次数超过数组长度的一半，
请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""
"""
思路一： 使用key解决


"""

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        m_dict = {}
        max_nums = 0
        flag = 0
        for item in numbers:
            if item in m_dict.keys():
                m_dict[item] = m_dict[item] + 1
                if m_dict[item] > max_nums:
                    flag = item
                    max_nums = m_dict[item]
            else:
                m_dict[item] = 1
                if max_nums == 0:
                    max_nums = 1
                    flag = item
        if max_nums > len(numbers)//2:
            return flag
        else:
            return 0
solution = Solution()
numbers = [1,2,3,2,2,2,5,4,2]

print(solution.MoreThanHalfNum_Solution(numbers))