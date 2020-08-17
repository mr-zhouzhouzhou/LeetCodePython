"""
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.（从0开始计数）
"""


# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s is None or len(s)==0:
            return -1
        m_dict = {}
        m_temp = {}
        m_list = []

        for index, item in enumerate(s):
            if item in m_dict.keys():
                m_dict[item] += 1
                if item in m_list:
                    m_list.remove(item)
            else:
                m_dict[item] = 1
                m_temp[item] = index
                m_list.append(item)
        if len(m_list) > 0:
            return m_temp[m_list[0]]
        return -1

sSolution = Solution()
a = sSolution.FirstNotRepeatingChar("google")
print(a)