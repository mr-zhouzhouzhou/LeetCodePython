"""
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数
（时间复杂度应为O（1））。
"""


class Solution:
    def __init__(self):
        self.sort = []
        self.store = []

    def push(self, node):
        self.store.insert(0, node)
        if len(self.sort) == 0:
            self.sort.append(node)
            return
        temp = -1
        for index, value in enumerate(self.sort):

            if value >= node:
                temp = index
                break

        if temp == - 1:

            self.sort.append(node)
        else:
            self.sort.insert(temp, node)

    # write code here
    def pop(self):
        pop_num = self.store[0]
        self.store.pop(0)
        self.sort.remove(pop_num)
        return pop_num

    # write code here
    def top(self):
        return self.sort[0]

    # write code here
    def min(self):
        if len(self.sort) == 0:
            return None
        return self.sort[0]

# write code here

3,3,2,2,2,3,3,0

"""
"PSH3","MIN","PSH4","MIN","PSH2","MIN","PSH3","MIN","POP","MIN","POP","MIN","POP","MIN","PSH0","MIN"]
"""

solution = Solution()
solution.push(3)
print(solution.min())

solution.push(4)
print(solution.min())

solution.push(2)
print(solution.min())


solution.push(3)
print(solution.min())

solution.pop()
print(solution.min())
solution.pop()
print(solution.min())
solution.pop()
print(solution.min())
solution.push(0)
print(solution.min())
print(solution.sort)




# node = 3
# sort = []
# for node in [3,3,2,2,2,3,3,0]:
#     temp = 0
#     if len(sort) == 0:
#         sort.append(node)
#         continue
#     for index, value in enumerate(sort):
#         temp = index
#         if value >= node:
#             break
#
#     if temp == len(sort):
#         sort.append(node)
#     else:
#         sort.insert(temp, node)
#
# print(sort)
