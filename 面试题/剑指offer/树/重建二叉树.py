


"""
问题描述：现有 前序遍历 和 中序遍历， 如何构建二叉树
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        index = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:index + 1], tin[:index])
        root.right = self.reConstructBinaryTree(pre[index+1:], tin[index+1:])
        return root