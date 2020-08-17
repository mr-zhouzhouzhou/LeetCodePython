

"""
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""


# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode == None:
            return None
        if  pNode.right is None and pNode.next is None:
            return None
        if pNode.right is None:
            if pNode.next.left == pNode:
                return pNode.next
            else:
                father = pNode.next
                while father:
                    if father.next:
                        if father == father.next.left:
                            return father.next
                        else:
                            father = father.next
                    else:
                        return None
        else:
            temp = pNode.right
            while temp.left:
                temp = temp.left
            return temp


