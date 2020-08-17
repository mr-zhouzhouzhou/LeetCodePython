"""
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None:
            return None
        fast = pHead.next
        slow = pHead
        if fast is None:
            return None
        while fast:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next
            if fast is None or slow is None:
                return None
            fast = fast.next
        return None
