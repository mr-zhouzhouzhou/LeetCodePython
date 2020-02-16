"""
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""
#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
    # write code here
        head = None
        node = None
        if pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                head = pHead1
                pHead1 = pHead1.next
            else:
                head = pHead2
                pHead2 = pHead2.next
        else:
            return pHead1 if pHead1 else pHead2
        node = head
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                temp = pHead1
                pHead1 = pHead1.next
                node.next = temp
                node = temp

            else:
                temp = pHead2
                pHead2 = pHead2.next
                node.next = temp
                node = temp

        while pHead1:
            temp = pHead1
            pHead1 = pHead1.next

            node.next = temp
            node = temp

        while pHead2:
            temp = pHead2
            pHead2 = pHead2.next
            node.next = temp
            node = temp
        node.next = None
        return head



node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node4 = ListNode(7)
node5 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

tem1 = node1


node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(6)
node4 = ListNode(8)
node5 = ListNode(10)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

tem2 = node1

solution = Solution()

node = solution.Merge(tem1, tem2)

while node:
    print(node.val)
    node = node.next