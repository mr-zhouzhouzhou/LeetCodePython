






class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        from collections import Counter
        c = Counter(s)
        buckets = [[] for _ in range(len(s) + 1)]
        for x, y in c.items():
            buckets[y].append(x)
        res = []
        for i in range(len(s), -1, -1):
            for item in buckets[i]:
                res.extend(item*i)
        return "".join(res)



s = "cccaaa"
solution = Solution()
solution.frequencySort(s)