


import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        low = 0
        high = int(math.sqrt(c))

        while low <=high:
            temp = low * low + high * high
            if temp == c:
                return True
            elif temp > c:
                high -= 1
            else:
                low += 1
        return False