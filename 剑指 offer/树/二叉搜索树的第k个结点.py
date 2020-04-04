"""
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""

"""
这是一个递归过程  首先要判断 根节点是第几个

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k > self.get_index(pRoot, "all") or k < 1:
            return None
        while self.get_index(pRoot, "left") != k:
            if self.get_index(pRoot, "left") > k:
                pRoot = pRoot.left

            else:
                k = k - self.get_index(pRoot, "left")
                pRoot = pRoot.right
        return pRoot

    def get_index(self, root, label):
        if root == None:
            return 0
        if label == "left":
            if root.left is None:
                return 1
            node = [root.left]
            count = 1
        else:
            count = 0
            node = [root]
        node_temp = []
        while len(node) != 0:
            for item in node:
                count = count + 1
                if item.left is not None:
                    node_temp.append(item.left)
                if item.right is not None:
                    node_temp.append(item.right)
            node = node_temp
            node_temp = []
        return count
    
{8,6,10,5,7,9,11},3
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



node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.right = node2
node2.right = node3
node3.right = node4
node4.right = node5


node1.left = None
node2.left = None
node3.left = None
node4.left = None
node5.left = None

solution = Solution()
print(solution.get_index(node1, "all"))
re = solution.KthNode(node1, 3)

print(re.val)