
"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
"""
"""
耗时太高了：执行用时 :
1292 ms, 在所有 Python 提交中击败了5.23%的用户
内存消耗 :16.1 MB, 在所有 Python 提交中击败了6.38%的用户
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter

        m_dict = Counter(nums)
        temp = list(m_dict.keys())
        for i in range(len(temp) - 1):
            for j in range(i+1, len(temp)):
                if m_dict[temp[i]] < m_dict[temp[j]]:
                    temp[i], temp[j] = temp[j], temp[i]
        if k > len(temp):
            return []
        else:
            return temp[:k]


class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        c = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for x, y in c.items():
            buckets[y].append(x)
        res = []
        for i in range(len(nums), -1, -1):
            if len(res) > k:
                break
            res.extend(buckets[i])
        return res[:k]

solution = Solution()
nums = [5,5,10,2,2,3]
k = 2

print(solution.topKFrequent(nums, k))
