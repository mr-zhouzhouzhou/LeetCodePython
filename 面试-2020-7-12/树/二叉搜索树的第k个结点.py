"""


题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        length = self.getNums(pRoot)
        if k < 1 or k > length:
            return None
        temp = pRoot
        while True:
            len_left = self.getNums(temp.left)
            if len_left == k:
                return temp.left.val
            if len_left == k - 1:
                return temp.val

            if len_left > k:
                length = len_left
                temp = temp.left
            if len_left +1 <k:
                length = length -len_left - 1
                k = k -len_left - 1
                temp = temp.right


    def getNums(self, pRoot):
        m_list = []
        if pRoot == None:
            return 0
        m_list.append(pRoot)
        count = 0
        while len(m_list) != 0:
            a = m_list.pop(0)
            count += 1
            if a.left:
                m_list.append(a.left)
            if a.right:
                m_list.append(a.right)
        return count


# 5，3，7，2，4，6，8
# {8,6,10,5,7,9,11},1
# {8,6,10,5,7,9,11},1

a = [12,3]


print(a.pop(0))
print(a)