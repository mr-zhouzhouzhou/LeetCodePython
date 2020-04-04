"""
LetCode:524题
"""


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        maxlength = 0
        longstr = ""
        temp = []
        for item in d:
            if item > longstr and len(longstr) == len(item):
                continue
            flag = self.check(item, s)
            if flag:
                if len(item) > maxlength:
                    longstr = item
                    maxlength = len(item)
                elif len(item) == maxlength:
                    longstr = item
        return longstr

    def check(self, str1, str2):
        str1 = list(str1)
        str2 = list(str2)
        if len(str2) < len(str1):
            return False
        i = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                i += 1
                if i == len(str1):
                    return True
            j += 1
        if i < len(str1):
            return False
        return True


s = "aaa"
d = ["aaa", "aa", "a"]

solution = Solution()
print(solution.findLongestWord(s, d))
print("ab"< "ba")