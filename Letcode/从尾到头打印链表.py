

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val



def printNode(node):
    if node is None:
        return
    printNode(node.next)
    print(node.val)



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

node6.next =None

printNode(node1)