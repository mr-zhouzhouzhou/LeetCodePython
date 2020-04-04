


# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):

        # write code here
        if size == 1:
            return num
        m_list = []
        resoult = []
        for index, item in enumerate(num):
            if len(m_list) == 0:
                m_list.append(index)
            print(index, m_list)
            if index - m_list[0] >= size:
                m_list.pop(0)
            if item > num[m_list[0]]:
                m_list = [index]
            else:
                while item > num[m_list[-1]]:
                    m_list.pop(-1)
                if index != 0:
                    m_list.append(index)
            if index >= size - 1:
                resoult.append(num[m_list[0]])
        return resoult
so = Solution()
num = [10,14,12,11]
size = 1

print(so.maxInWindows(num, size))