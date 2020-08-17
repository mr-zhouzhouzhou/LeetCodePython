# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



"""
题目描述
请实现一个函数，用来判断一棵二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot is None:
            return True

        return self.checkMetrical(pRoot.left, pRoot.right)

    def checkMetrical(self, node_left, node_right):
        if node_left is None and node_right is None:
            return True
        if node_left is None or node_right is None:
            return False
        if node_right.val != node_left.val:
            return False
        return self.checkMetrical(node_left.left, node_right.right) \
               and self.checkMetrical(node_left.right, node_right.left)