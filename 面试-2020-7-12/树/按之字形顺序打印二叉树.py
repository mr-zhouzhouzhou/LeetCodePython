"""
题目描述
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []


        flag = 0
        temp_list = []
        m_list =[]
        m_list.append(pRoot)
        temp = []
        resoult = []

        while len(m_list)!=0 or len(temp_list) != 0:
            if len(m_list) != 0:
                a = m_list.pop(0)
                if flag == 0:
                    temp.append(a.val)
                else:
                    temp.insert(0, a.val)
                if a.left:
                    temp_list.append(a.left)
                if a.right:
                    temp_list.append(a.right)
            else:

                if flag==0:
                    flag = 1
                else:
                    flag = 0
                resoult.append(temp)
                temp = []

                m_list = temp_list
                temp_list = []
        if len(temp) != 0:
            resoult.append(temp)
        return   resoult