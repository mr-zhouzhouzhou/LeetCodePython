"""
题目描述
根据二叉树的前序遍历和中序遍历的结果，重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的
数字。
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        tin_dict = {}
        for index, item in enumerate(tin):
            tin_dict[item] = index
        return self.buildTree(pre, 0, len(pre), 0, tin_dict)

    def buildTree(self, pre, preL, preR, ind, tin_dict):
        if preL > preR:
            return None
        node = TreeNode(pre[preL])
        index = tin_dict[pre[preL]]
        leftSize = index - ind
        node.left = self.buildTree(pre, preL + 1, preL + leftSize, ind, tin_dict)
        node.right = self.buildTree(pre, preL + leftSize + 1, preR, index + 1, tin_dict)
        return node



class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre.pop(0))
        index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre, tin[:index])
        root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
        return root
