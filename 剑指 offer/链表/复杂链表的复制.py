"""
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""

# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None :
            return pHead
        node_temp = []
        node_list = []
        temp = pHead
        while temp is not None:
            node = RandomListNode(temp.label)
            node_list.append(node)
            node_temp.append(temp)
            temp = temp.next
        temp = pHead
        index = 0
        while temp is not None:
            if index < len(node_list) - 1:
                node_list[index].next = node_list[index + 1]

            else:
                node_list[index].next = None
            if temp.random is None:
                node_list[index].random = None
            else:
                node_index = node_temp.index(temp.random)
                node_list[index].random = node_list[node_index]
            index = index + 1
            temp = temp.next
        return node_list[0]