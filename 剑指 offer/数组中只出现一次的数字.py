"""

题目描述
一个整型数组里除了两个数字之外，
其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        m_dict = {}
        m_list = []
        for item in array:
            if item in m_dict.keys():
                if item in m_list:
                    m_list.remove(item)
            else:
                m_dict[item] = 1
                m_list.append(item)
        return m_list