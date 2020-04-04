# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        itemList = []
        self.get_list(listNode, itemList)
        return itemList

    def get_list(self, listNode, itemList):
        if listNode != None:
            self.get_list(listNode.next, itemList)
            itemList.append(listNode.val)
        else:
            return

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None


solution = Solution()
itemList = solution.printListFromTailToHead(node1)
print(itemList)