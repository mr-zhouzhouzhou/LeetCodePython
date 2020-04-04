


"""
约瑟夫环
"""





class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        head = Node(None)
        temp = head
        for i in range(n):
            node = Node(i)
            temp.next = node
            temp = node
        head = head.next
        temp.next = head
        key = -1
        while head.next != head:
            key += 1
            if key == m-1:
                node = head.next
                head.val = node.val
                head.next = node.next
                node.next = None
                key = 0
            head = head.next
        return head.val




class Solution:
    def LastRemaining_Solution(self, n, m):
        if n ==0 or m <=0:
            return -1
        last = 0
        for item in range(2, n + 1):
            last = (last + m) % item
        return last
