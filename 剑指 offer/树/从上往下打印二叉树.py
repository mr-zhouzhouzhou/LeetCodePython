"""
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""
"""
思路：层次遍历

"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here:
        if root is None:
            return []
        node_list = []
        nodes = []
        node_list.append(root)
        while len(node_list) != 0:
            node = node_list.pop(0)
            nodes.append(node.val)
            if node.left is not None:
                node_list.append(node.left)
            if node.right is not None:
                node_list.append(node.right)

        return nodes