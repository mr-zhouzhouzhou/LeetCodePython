"""
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return True
        bol = self.SquenceOfBS(sequence)
        return bol

    def SquenceOfBS(self, sequence):
        if len(sequence) <= 1:
            return True
        left = []
        right = []
        flag = True
        for item in sequence[: -1]:
            if item < sequence[-1]:
                if flag:
                    left.append(item)
                else:
                    return False
            elif item > sequence[-1]:
                flag = False
                right.append(item)
            else:
                return False
        bol = self.SquenceOfBS(left)
        if bol is False:
            return False
        bol = self.SquenceOfBS(right)
        if bol is False:
            return False
        return True



solution = Solution()
bol = solution.SquenceOfBS([5,4,3,2,1])
print(bol)