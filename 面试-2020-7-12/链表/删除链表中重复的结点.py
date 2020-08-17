"""
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""


#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        head = ListNode(None)
        temp = head
        if pHead is None:
            return None
        temp_val = pHead.val
        count = 0
        while pHead:
           if pHead.val == temp_val:
               pHead = pHead.next
               count = count + 1
           else:
               if count == 1:
                   print("#####: ", pHead.val)
                   node = ListNode(temp_val)
                   temp.next = node
                   temp = node
                   temp_val = pHead.val
                   count = 1
                   pHead = pHead.next
               else:
                   count = 1
                   temp_val = pHead.val
                   pHead = pHead.next
        if count == 1:
            node = ListNode(temp_val)
            temp.next = node
            node.next = None
        else:
            temp.next = None
        return head.next


{1,2,3,3,4,4,5}
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)
node1.next =  node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = None

solution = Solution()

a  = solution.deleteDuplication(node1)

while a:
    print(a.val)
    a = a.next

print(1==None)