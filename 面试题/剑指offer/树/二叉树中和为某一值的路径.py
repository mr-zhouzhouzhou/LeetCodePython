


"""
采用的是  二叉树的非递归的后续排序
"""
class Solution(object):
    def FindPath(self, root, expectNumber):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        target = expectNumber
        if root is None:
            return []
        count = 0
        flag = 0
        resoult = []
        visited = [root]
        count = root.val
        while len(visited) != 0:
            item = visited[-1]
            if item.left is None and item.right is None:
                if count == target:
                    resoult.append([item.val for item in visited])
                flag = item
                visited.pop()
                count = count - item.val
            elif item.left is not None and item.left is not flag and item.right is not flag:
                count = count + item.left.val
                visited.append(item.left)
            elif item.right is not None and item.right is not flag:
                count = count + item.right.val
                visited.append(item.right)
            elif item.right is None or (item.right is not None and item.right == flag):
                # resoult.append(item.val)
                count = count - item.val
                flag = item
                visited.pop()
        return resoult


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.left = node2
node1.right = node2
node2.right = None
node2.left = None
node3.left = None
node3.right = None

resoult = Solution()
print(resoult.FindPath(node1, 3))