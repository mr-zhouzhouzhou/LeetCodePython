
"""
题目描述
输入一个链表，反转链表后，输出新链表的表头。
"""
#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None:
            return None
        head = pHead
        pHead = pHead.next
        head.next = None
        while pHead is not None:
            temp = pHead
            pHead = pHead.next
            temp.next = head
            head = temp
        return head

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

# while node1:
#     print(node1.val)
#     node1 = node1.next

solution = Solution()
solution.ReverseList(node1)
#
