

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 0:
            return 0
        count = 0
        for index in range(1, n + 1):
            count += self.getNum(index)
        return count


    def getNum(self, n):

        count = 0
        while n > 0:
            temp = n % 10
            if temp == 1:
                count += 1
            n = n / 10
        return count