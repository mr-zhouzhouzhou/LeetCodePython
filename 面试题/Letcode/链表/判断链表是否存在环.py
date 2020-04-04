# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head

        while slow is not None and fast is not None:
            slow = slow.next
            if slow is None:
                return False
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next

            if id(slow) == id(fast):
                return True

        return False
