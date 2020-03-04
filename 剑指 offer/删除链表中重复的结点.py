"""
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""
"""
1： 如果只有一个节点 或者没有 直接返回
2： 如果两个节点的话 ，不一致就返回，有一样的 返回None
3： 如果有3个或者3个以上的话
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        temp = pHead
        temp_val = "x"
        while temp is not None and temp.next is not None:
            if temp.val == temp.next.val:
                temp_val = temp.val
                temp = temp.next
            else:
                if temp == pHead:
                    break
                temp = temp.next
                if temp is not None and temp.next is not None:
                    if temp.val != temp.next.val:
                        break
        if temp is None or temp.val == temp_val:
            return None

        headnode = temp
        head = temp
        temp = temp.next
        while temp is not None:
            node = temp
            if temp.next is not None:

                if temp.val != headnode.val and temp.next.val != temp.val:

                    headnode.next = temp
                    headnode = temp
                else:
                    while temp is not None and temp.next is not None and temp.val == temp.next.val:
                        temp = node.next
                temp = temp.next

            else:
                    headnode.next = temp
                    headnode = temp
                    headnode.next = None
                    temp = None
        headnode.next = None
        return head




{1,2,3,3,4,4,5}

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node4 = ListNode(1)
node5 = ListNode(1)
node6 = ListNode(1)
node7 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next =None

solution = Solution()

head = solution.deleteDuplication(node1)

print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next)
