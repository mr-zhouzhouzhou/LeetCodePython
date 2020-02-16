"""

题目描述
输入一个链表，输出该链表中倒数第k个结点。
"""

"""

思路：
1：确定list的长度
2：然后 双指针遍历
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        array_len = 0
        temp = head
        while temp is not None:
            array_len = array_len + 1
            temp = temp.next
        if array_len <= k:
            return None if array_len < k else head

        fast = head
        slow = head

        while k > 0:
            fast = fast.next
            k = k - 1
        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow


