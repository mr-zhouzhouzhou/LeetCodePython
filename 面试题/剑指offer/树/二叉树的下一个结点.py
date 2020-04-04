"""
二叉树的下一个节点：

"""

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

"""
1: 如果节点有 右节点的话 ，下一个节点是右节点的最左节点
2：如果节点没有右节点，那么


"""
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return None
        #如果节点没有右节点
        if pNode.right is None:
            while pNode.next is not None and pNode is pNode.next.right:
                pNode = pNode.next
            if pNode is None:
                return None
            return pNode.next
        #如果pNode有右节点
        node = pNode.right
        while node.left:
            node = node.left
        return node
