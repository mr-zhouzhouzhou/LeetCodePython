"""
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""


#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        node_list = []
        temp = pHead
        while temp:
            if temp in node_list:
                break
            else:
                node_list.append(temp)
            temp = temp.next
        temp = pHead
        count = 0
        while temp:
            index = node_list.index(temp)
            if count != index:
                return temp
            count = count + 1
            temp = temp.next