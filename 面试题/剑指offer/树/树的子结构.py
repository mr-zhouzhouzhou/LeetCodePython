# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 is None or pRoot2 is None:
            return False
        if self.isSub(pRoot1, pRoot2):
            return True
        return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def isSub(self, root1, root2):

        if root2 is None:
            return True
        if root1 is None:
            return False
        if root1.val != root2.val:
            return False

        return self.isSub(root1.left, root2.left) and self.isSub(root1.right, root2.right)

node1 = TreeNode(8)
node2 = TreeNode(8)
node3 = TreeNode(7)
node4 = TreeNode(9)
node5 = TreeNode(2)
node6 = TreeNode(4)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node5.left = node6
node5.right = node7


node3.left = None
node3.right = None

node4.left = None
node4.right = None

node6.left = None
node6.right = None

node7.left = None
node7.right = None



node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(2)
node8.left = node9
node8.right = node10

node9.left = None
node9.right = None
node10.left = None
node10.right = None




solution = Solution()


resoult = solution.HasSubtree(node1, node8)

print(resoult)
