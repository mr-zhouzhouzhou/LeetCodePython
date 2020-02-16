"""
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，
请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，
序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）
"""
"""
思路：


"""
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here()
        store = []
        temp = popV.copy()
        for index, value in enumerate(temp):
            if len(store) > 0:
                if value == store[0]:
                    store.pop(0)
                    popV.pop(0)
                    continue
            if value in pushV:
                index = 0
                for index, item in enumerate(pushV):
                    if item == value:
                        store.insert(0, item)
                        break
                    else:
                        store.insert(0, item)
                pushV = pushV[index+1:]
                store.pop(0)
                popV.pop(0)
            else:
                return False
        return True






pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]


# pushV = [1]
# popV = [4]
solution = Solution()

bo = solution.IsPopOrder(pushV, popV)
print(bo)