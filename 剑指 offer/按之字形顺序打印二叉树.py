"""
题目描述
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        left = []
        right = []
        result = []
        if pRoot is None:
            return []
        left.append(pRoot)

        while len(left) != 0 or len(right) != 0:
            if len(left) != 0:
                temp = []
                for item in left:
                    if item is not None:
                        temp.append(item.val)
                        if item.left is not None:
                            right.append(item.left)
                        if item.right is not None:
                            right.append(item.right)
                left = []
                result.append(temp)
            else:
                temp = []
                for item in reversed(right):
                    if item is not None:
                        temp.append(item.val)
                for item in right:
                    if item.left is not None:
                        left.append(item.left)
                    if item.right is not None:
                        left.append(item.right)
                right = []
                result.append(temp)
        return result

{8,6,10,5,7,9,11}
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

