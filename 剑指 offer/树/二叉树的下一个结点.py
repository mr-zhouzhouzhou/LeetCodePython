"""
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""

"""
两步走：
1：取右节点的最左子节点

2：取它的父亲节点
"""

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return pNode
        node = pNode
        if node.right is None:
            while node.next is not None and node is node.next.right:
                node = node.next
            if node is None:
                return None
            return node.next

        temp = pNode.right
        while temp.left is not None:
            temp = temp.left
        return temp