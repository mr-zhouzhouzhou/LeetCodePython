"""
题目描述
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""
"""
思路：
1：判断每个数字含有1的个数
2： 用字符串的方式 或者 用除法  （两个都不快）

"""

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        all = 0
        for index in range(n+1):
            all = all + self.get_nums(index)
        return all

    def get_nums(self, n):
        nums = 0
        while n > 0:
            temp = n % 10
            n = n/10
            if temp == 1:
                nums = nums + 1
        return nums

    def get_num(self, n):
        n = str(n)
        nums = 0
        for item in str(n):
            if item == "1":
                nums = nums + 1
        return nums



for item in "dkedbiqwldq":
    print(item)