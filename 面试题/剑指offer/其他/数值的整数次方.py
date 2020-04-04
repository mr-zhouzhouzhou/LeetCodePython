class Solution:
    def Power(self, base, exponent):
        # write code here
        res = 1.0
        flag = True
        if exponent == 0:
            return 1
        if exponent < 0:
            exponent *= -1
            flag = False
        num_bin = str(bin(exponent))[2:]
        temp = 1.0
        for i in range(0, len(num_bin)):
            index = - i - 1
            if index == -1:
                temp = base
            else:
                temp *= temp
            if num_bin[index] == '1':
                res *= temp
        return res if flag else 1/res




soultion = Solution()

resoult = soultion.Power(3,7)
print(resoult)
import math
print(math.pow(3, 7))