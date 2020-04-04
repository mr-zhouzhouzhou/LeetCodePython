
"""
耗时：128ms 时间复杂度 和空间复杂度 都很高
"""


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        low = 0
        high = len(s) - 1

        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return self.check(s, low+1, high) or self.check(s, low, high - 1)
        return True

    def check(self, nums, low, high):
        while low < high:
            if nums[low] == nums[high]:
                low += 1
                high -= 1
            else:
                return False
        return True