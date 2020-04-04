



"""
思路：如果

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def VerifySquenceOfBST(self, node):
        # write code here
        if node is None:
            return None
        flag = 0
        visited = [node]
        while len(visited) != 0:
            item = visited[-1]

            if item.left is None and item.right is None:
                print(item.val)
                flag = item
                visited.pop()
            elif item.left is not None and item.left is not flag and item.right is not flag:
                visited.append(item.left)
            elif item.right is not None and item.right is not flag:
                visited.append(item.right)
            elif item.right is None or (item.right is not None and item.right == flag):
                print(item.val)
                flag = item
                visited.pop()



class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        flag = 0
        resoult = []
        visited = [root]
        while len(visited) != 0:
            item = visited[-1]

            if item.left is None and item.right is None:
                resoult.append(item.val)
                flag = item
                visited.pop()
            elif item.left is not None and item.left is not flag and item.right is not flag:
                visited.append(item.left)
            elif item.right is not None and item.right is not flag:
                visited.append(item.right)
            elif item.right is None or (item.right is not None and item.right == flag):
                resoult.append(item.val)
                flag = item
                visited.pop()
        return resoult

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.left = node2
node1.right = None

node2.left = None
node2.right = None

node3.left = None
node3.right = None


soultion = Solution()
soultion.VerifySquenceOfBST(node1)