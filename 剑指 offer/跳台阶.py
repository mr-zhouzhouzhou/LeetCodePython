"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""


"""
思路：
    这题目其实是一个斐波那契额数字
    f(n) = f(n-1) + f(n-2)
    
    和斐波那契的区别在于，f(1) = 1, f(2) = 2

"""


class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 0:
            return 0
        if number <= 2:
            return 1 if number == 1 else 2
        first, second = 1, 2
        number = number - 2
        jump_num = 0
        for index in range(number):
            jump_num = first + second
            first, second = second, jump_num
        return jump_num