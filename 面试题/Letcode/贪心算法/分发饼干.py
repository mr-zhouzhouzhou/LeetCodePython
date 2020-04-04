class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: ints.sort()
        """
        g.sort()
        s.sort()
        count = 0
        i = 0
        j = 0
        while i < len(s)and j < len(g):
            if s[i] >= g[j]:
                count += 1
                j += 1
            i += 1


g, s = [1,2,3], [1,1]

solution =Solution()
re = solution.findContentChildren(g, s)

print(re)