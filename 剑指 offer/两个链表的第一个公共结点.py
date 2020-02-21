"""
题目描述
输入两个链表，找出它们的第一个公共结点。
（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
"""


#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        len_p1 = self.get_len(pHead1)
        len_p2 = self.get_len(pHead2)
        if len_p1 == 0 or len_p2 == 0:
            return None
        if len_p1 > len_p2:
            while len_p1 != len_p2:
                pHead1 = pHead1.next
                len_p1 = len_p1 - 1
        else:
            while len_p1 != len_p2:
                pHead2 = pHead2.next
                len_p2 = len_p2 - 1

        while pHead1 != pHead2:
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return pHead1


    def get_len(self, node):
        node_len = 0
        while node is not None:
            node_len = node_len + 1
            node = node.next
        return node_len

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node6.next = node7
node7.next = None

node1.next = node2
node2.next = node3
node3.next = node6


node4.next = node5
node5.next = node6

solution = Solution()
node = solution.FindFirstCommonNode(node1, node4)
print(node)