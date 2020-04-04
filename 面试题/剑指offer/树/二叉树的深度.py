

def treeDepth(root):
    return 0 if root is None else 1 + max(treeDepth(root.left), treeDepth(root.right))