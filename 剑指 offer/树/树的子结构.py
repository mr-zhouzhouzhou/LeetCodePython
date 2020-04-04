"""
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""

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
        nodelist = self.checkroot(pRoot1, pRoot2)

        for item in nodelist:
            print(item.val)
        if len(nodelist) == 0:
            return False

        for item in nodelist:
            flag = self.checkStruct(item, pRoot2)
            if flag is True:
                return True
        return False

    def checkStruct(self, node1, node2):
        if node2 is None:
            return True
        else:
            if node1 is not None:
                if node1.val != node2.val:
                    return False
            else:
                return False
        flag = self.checkStruct(node1.left,node2.left) and self.checkStruct(node1.right, node2.right)
        return flag

    def checkroot(self, node1, node2):
        rootlist = []
        if node1 == node2:
            rootlist.append(node1)
        nodelist = [node1]
        rootlist = []
        while len(nodelist) != 0:
            temp = nodelist.pop(0)
            if temp.val == node2.val:
                rootlist.append(temp)
            if temp.left is not None:
                nodelist.append(temp.left)
            if temp.right is not None:
                nodelist.append(temp.right)
        return rootlist
#{8,8,7,9,2,#,#,#,#,4,7},{8,9,2}
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
