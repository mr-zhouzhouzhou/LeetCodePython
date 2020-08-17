"""
题目描述
输入两个链表，找出它们的第一个公共结点。
（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        pHead1_length = self.Length(pHead1)
        pHead2_length = self.Length(pHead2)
        if pHead1_length > pHead2_length:
            for _ in  range(pHead1_length - pHead2_length):
                pHead1 = pHead1.next
        elif pHead1_length < pHead2_length:
            for _ in  range(pHead2_length - pHead1_length):
                pHead2 = pHead2.next

        while pHead1:
            if pHead1 ==pHead2:
                return pHead1
            pHead1 =pHead1.next
            pHead2 = pHead2.next
        return None

    def Length(self, pRoot):
        length = 0
        if pRoot is None:
            return length

        while pRoot:
            length += 1
            pRoot = pRoot.next
        return length