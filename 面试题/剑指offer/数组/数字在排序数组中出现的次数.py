
"""
Input:
nums = 1, 2, 3, 3, 3, 3, 4, 6
K = 3
Output: 4
"""

def binarySearch(nums, k):
    low = 0
    high = len(nums)
    while low < high:
        m = (low + high) // 2
        if nums[m] >= k:
            h = m
        else:
            l = m + 1
    return l


def solution(nums, k):
    first = binarySearch(nums, k)
    last = binarySearch(nums, k + 1)
    return 0 if len(nums) == first or nums[first]!=k else last - first
