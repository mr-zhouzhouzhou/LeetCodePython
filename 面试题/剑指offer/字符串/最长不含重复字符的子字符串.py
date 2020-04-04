


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        m_dict = {}
        length = len(s)
        start = 0
        end = 0
        max_length = 0
        for i in range(0, length):
            if s[i] in m_dict.keys():
                if m_dict[s[i]] >= start and m_dict[s[i]] <= end:
                    start = m_dict[s[i]] + 1
                end = i
                m_dict[s[i]] = i
            else:
                m_dict[s[i]] = i
                end = i
            if max_length < end - start + 1:
                max_length = end - start + 1
        return max_length

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        max_length = 0
        cur_length = 0
        for i in range(len(s)):
            if s[i] not in dic or i - dic[s[i]] > cur_length:
                cur_length += 1
            else:
                cur_length = i - dic[s[i]]
            dic[s[i]] = i
            if max_length < cur_length:
                max_length = cur_length
        return max_length


soultion = Solution()

re = soultion.lengthOfLongestSubstring("abcabcbb")
print(re)
