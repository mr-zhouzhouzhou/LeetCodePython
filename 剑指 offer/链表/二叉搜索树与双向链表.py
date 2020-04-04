"""
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""

"""
思路： 先中序遍历， 然后把节点记录下来 一个for循环
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None
        nodelist = []
        self.middelSort(pRootOfTree, nodelist)
        nodelist[0].left = None
        if len(nodelist) == 1:
            nodelist[0].right = None
        else:
            nodelist[0].right = nodelist[1]
        for item in range(1, len(nodelist)):
            if item < len(nodelist) - 1:
                nodelist[item].left = nodelist[item - 1]
                nodelist[item].right = nodelist[item + 1]

            else:
                nodelist[item].right = None
                nodelist[item].left = nodelist[item - 1]

        return nodelist[0]

    def middelSort(self, node, nodelist):
            if node is None:
                return
            if node.left is not None:
                self.middelSort(node.left, nodelist)
            nodelist.append(node)

            if node.right is not None:
                self.middelSort(node.right, nodelist)


{10,6,14,4,8,12,16}
node1 = TreeNode(10)
node2 = TreeNode(6)
node3 = TreeNode(14)
node4 =  TreeNode(4)
node5 =  TreeNode(8)
node6 = TreeNode(12)
node7 = TreeNode(16)

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
nodelist = []
re = solution.Convert(node1)
