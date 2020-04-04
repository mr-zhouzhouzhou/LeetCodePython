

import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = collections.Counter(s)
        for k, v in ans.items():
            if v == 1:
                return k
        return
