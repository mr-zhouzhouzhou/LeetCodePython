"""
题目描述
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        nums = []
        result = []
        self.solution(root, expectNumber, nums, result)
        return result

    def solution(self, root, expectNumber, nums, result):
        # write code here
        if root is None:
            return
        else:
            nums.append(root.val)
            if sum(nums) == expectNumber and root.left is None and root.right is None:
                temp = [item for item in nums]
                result.append(temp)
        left = root.left
        if left is None:
            return
        else:
            self.solution(left, expectNumber, [item for item in nums], result)
        right = root.right
        if right is None:
            return
        else:
            self.solution(right, expectNumber, [item for item in nums], result)
