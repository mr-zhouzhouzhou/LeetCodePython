"""

给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
"""


# -*- coding:utf-8 -*-
# class Solution:
#     def multiply(self, A):
#         # write code here
#         if len(A) < 2:
#             return []
#         B = [0] * len(A)
#         for index in range(len(A)):
#             B[index] = self.solution(A, index)
#         return B
#
#     def solution(self, A, index):
#         resoult = 1
#         for i,val in enumerate(A):
#             if i != index:
#                 resoult *= val
#         return resoult

class Solution:
    def multiply(self, A):

        B = [1] * len(A)
        for index in range(1, len(A)):
            B[index] = B[index-1] * A[index-1]
        temp = 1
        for index in range(len(A) - 2, -1, -1):
            temp *= A[index + 1]
            B[index] = B[index] * temp
        return B


A = [1,2,3,4,5]
solution = Solution()

print(solution.multiply(A))