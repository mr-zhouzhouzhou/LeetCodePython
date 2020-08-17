"""
题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        if abs(self.treeDeep(pRoot.left)-self.treeDeep(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def treeDeep(self, pRoot):
        if pRoot == None:
            return 0
        leftDeep = self.treeDeep(pRoot.left)
        rightDeep = self.treeDeep(pRoot.right)

        return max(leftDeep+1, rightDeep+1)