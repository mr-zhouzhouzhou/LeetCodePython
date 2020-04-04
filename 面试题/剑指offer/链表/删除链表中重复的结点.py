

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here

        head = ListNode(None)
        temp = head
        while pHead and pHead.next:
            if pHead.val != pHead.next.val:
                temp.next = pHead
                temp = pHead
                pHead = pHead.next
            else:
                while pHead and pHead.next:
                    if pHead.val == pHead.next.val:
                        pHead = pHead.next
                    else:
                        break
                pHead = pHead.next

        temp.next = pHead
        return head.next