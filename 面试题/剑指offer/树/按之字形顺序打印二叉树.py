


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def Print(self, pRoot):
#         # write code here
#         result = []
#         if pRoot is None:
#             return result
#         visited = [pRoot]
#         temp = []
#         flag = True
#         while len(visited) != 0:
#             a = []
#             for item in visited:
#                 a.append(item.val)
#                 if flag:
#                     if item.left:
#                         temp.append(item.left)
#                     if item.right:
#                         temp.append(item.right)
#                 else:
#                     if item.right:
#                         temp.append(item.right)
#                     if item.left:
#                         temp.append(item.left)
#             flag = False if flag else True
#             result.append(a)
#             temp.reverse()
#             visited = temp
#             temp = []
#         return result

[[8], [10, 6], [5, 7, 9, 11]]


class Solution:
    def Print(self, pRoot):
        # write code here
        result = []
        if pRoot is None:
            return result
        visited = [pRoot]
        temp = []
        flag = True
        while len(visited) != 0:
            a = []
            length = len(visited)
            for index in range(1, length + 1):
                item = visited[-index]
                a.append(item.val)
                if flag:
                    if item.left:
                        temp.append(item.left)
                    if item.right:
                        temp.append(item.right)
                else:
                    if item.right:
                        temp.append(item.right)
                    if item.left:
                        temp.append(item.left)
            flag = False if flag else True
            result.append(a)
            visited = temp
            temp = []
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