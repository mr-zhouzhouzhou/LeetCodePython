"""
题目描述
给定一个数组A[0,1,...,n-1],
请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。（注意：规定B[0]和B[n-1] = 1）
"""


# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = [1 for item in A]
        for index_a, value in enumerate(A):

            for index_b, value in enumerate(B):
                if index_b != index_a:
                    B[index_b] = B[index_b] * A[index_a]
        return B
