"""
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""


# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        resoult = ""
        numbers = self.sort(numbers)

        for item in numbers:
            resoult +=  str(item)
        return resoult
    def sort(self, numbers):
        for i in range(len(numbers) -1):
            temp = i
            for j in range(i+1, len(numbers)):
                if int(str(numbers[temp]) +str( numbers[j])) > int(str(numbers[j]) + str(numbers[temp])):
                    temp = j
            numbers[i], numbers[temp] = numbers[temp], numbers[i]
        return numbers

numbers = [3,5,1,4,2]

solution = Solution()
print(solution.PrintMinNumber(numbers))

