"""

复杂链表的复制：

"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        m_dict = {}
        head = RandomListNode()
        head.next = None
        pre = head
        temp = pHead
        while temp:
            node = RandomListNode(temp.val)
            m_dict[id(temp)] = temp
            pre.next = node
            pre = node
            temp = temp

        







a = 10

print(type(id(a)))