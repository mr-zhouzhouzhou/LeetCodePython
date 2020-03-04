"""
题目描述
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""


# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if "e" in s or "E" in s:
            if "e" in s:
                a, b = s.split("e")
            else:
                a, b = s.split("E")
            if a == "" or b == "" or '.' in b:
                return False
            bol = self.checkNumeric(a)
            if bol is False:
                return bol
            bol = self.checkNumeric(a)
            if bol is False:
                return False
            else:
                return True
        else:
            return self.checkNumeric(s)

    def checkNumeric(self, s):
        if s == "":
            return False
        if "+" in s or "-" in s:
            s = s[1:]
        if "." in s:
            str_list = s.split(".")
            if len(str_list) > 2:
                return False
            for item in str_list:
                for it in item:
                    if it < "0" or it > "9":
                        return False
        else:
            for it in s:
                if it < "0" or it > "9":
                    return False
        return True




solution = Solution()

print(solution.checkNumeric("100"))