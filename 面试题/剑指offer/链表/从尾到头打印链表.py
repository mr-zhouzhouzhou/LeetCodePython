"""

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def soultion(node):
    if node is None:
        return
    soultion(node.next)
    print(node.val)


def topSort(node):
    head = None
    while node:
        temp = node
        node = node.next
        temp.next = head
        head = temp
    return head



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
node3.next = None

soultion(node1)

node1 = Node(4)
node2 = Node(5)
node3 = Node(3)
node1.next = node2
node2.next = node3
node3.next = None
node4 = topSort(node1)
#
soultion(node4)