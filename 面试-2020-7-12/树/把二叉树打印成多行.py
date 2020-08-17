"""
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
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
        temp_list = []
        m_list =[]
        m_list.append(pRoot)
        temp = []
        resoult = []

        while len(m_list)!=0 or len(temp_list) != 0:
            if len(m_list) != 0:
                a = m_list.pop(0)
                temp.append(a.val)
                if a.left:
                    temp_list.append(a.left)
                if a.right:
                    temp_list.append(a.right)
            else:
                resoult.append(temp)
                temp = []

                m_list = temp_list
                temp_list = []
        if len(temp) != 0:
            resoult.append(temp)
        return   resoult