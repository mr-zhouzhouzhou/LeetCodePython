class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        index_list = []
        item_list = []
        temp = {"a":"", "e":"", "i":"", "o":"", "u":"", "A":"", "E":"", "I":"", "O":"", "U":""}
        for i in range(len(s)):
            if temp.get(s[i]) is not None:
                index_list.append(i)
                item_list.append(s[i])
        for i in range(1, len(index_list) + 1):
            s[index_list[-i]] = item_list[i-1]
        return "".join(s)

class Solution(object):
    def reverseVowels(self, s):
        if s is None:
            return s
        s = list(s)

        low = 0
        high = len(s) - 1
        temp = {"a": "", "e": "", "i": "", "o": "", "u": "", "A": "", "E": "", "I": "", "O": "", "U": ""}
        while low < high:
            while low < high and temp.get(s[low]) is None:
                low += 1
            while low < high and temp.get(s[high]) is None:
                high -= 1
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        return "".join(s)


s = "hello"

solution = Solution()

print(solution.reverseVowels(s))