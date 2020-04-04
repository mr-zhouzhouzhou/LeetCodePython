

"""
树的题目一般都用递归做：
判断
"""


def isBalance(root, balance):
    if root is None or balance[0] is False:
        return 0
    left = isBalance(root.left)
    right = isBalance(root.right)
    if abs(left, right) > 1:
        balance[0] = False
    return 1 + max(left, right)