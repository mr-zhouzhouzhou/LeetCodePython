"""
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。
"""

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) == 0 :
            return -1
        m_dict = {}
        m_list = []
        for index, value in enumerate(s):
            if value in m_dict.keys():
                m_dict[value] = m_dict[value] + 1
                if value in m_list:
                    m_list.remove(value)

            else:
                m_list.append(value)
                m_dict[value] = 1
        if len(m_list) == 0:
            return m_list[0]
        else:
            return -1




