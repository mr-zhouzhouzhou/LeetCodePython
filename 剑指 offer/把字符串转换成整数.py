"""
题目描述
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
"""

"""
微软面试的时候 考过这题

"""

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if s == None or len(s) ==0 :
            return 0
        flag = True
        s = s.strip()
        if s.startswith("+") or s.startswith("-"):
            flag = True if s.startswith("+") else False
            s = s[1:]

        sum = 0
        for item in s:
            if item >= "0" and item <= "9":
                sum = sum * 10 + int(item)
            else:
                return 0
        if flag:
            return sum
        else:
            return - sum

s = " 123"

solution = Solution()
result = solution.StrToInt(s)
print(type(result))
print(result)

print(len(s))