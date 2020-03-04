"""
题目描述
从上到下按层打印二叉树，
同一层结点从左至右输出。每一层输出一行。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):

        # write code here
        if pRoot is None:
            return []
        node_temp = []
        node = [pRoot]
        result = []

        while len(node) != 0:
            temp = []
            for item in node:
                print(item)
                temp.append(item.val)
                if item.left is not None:
                    node_temp.append(item.left)
                if item.right is not None:
                    node_temp.append(item.right)

            node = node_temp
            node_temp = []
            result.append(temp)
        return result

node1 = TreeNode(8)
node2 = TreeNode(6)
node3 = TreeNode(10)
node4 = TreeNode(5)
node5 = TreeNode(7)
node6 = TreeNode(9)
node7 = TreeNode(11)
node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

node4.left = None
node4.right = None

node5.left = None
node5.right = None

node6.left = None
node6.right = None

node7.left = None
node7.right = None

solution = Solution()
re = solution.Print(node1)

print(re)
