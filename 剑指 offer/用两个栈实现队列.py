"""
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        self.PUSHSTACK = []
        self.POPSTACK = []

    def push(self, node):
        self.PUSHSTACK.insert(0, node)
        # write code here

    def pop(self):
        if len(self.POPSTACK) == 0:
            if len(self.PUSHSTACK) == 0:
                return
            else:
                for item in self.PUSHSTACK:
                    self.POPSTACK.insert(0, item)
                self.PUSHSTACK = []
                data = self.POPSTACK.pop(0)
                return data
        else:
            data = self.POPSTACK.pop(0)
            return data

solution = Solution()
node = ["1", "2", "3", "4"]
for item in node:
    solution.push(item)

print(solution.PUSHSTACK)

solution.pop()
solution.pop()
solution.pop()
solution.pop()
print(solution.PUSHSTACK)
print(solution.POPSTACK)


