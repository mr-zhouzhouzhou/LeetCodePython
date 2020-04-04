"""
在一个长度为 n 的数组里的所有数字都在 0 到 n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字是重
复的，也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
"""

def solution(nums):
    m_dict = {}
    if nums is None or len(nums) < 2:
        return None
    for item in nums:
        if item in m_dict.keys():
            return item
    return None



"""
时间复杂度为O（n）
空间复杂度： 1
"""


def solution(nums):
    if nums is None or len(nums) < 2:
        return -1
    for index, item in enumerate(nums):
        while index != nums[index] and nums[index] != nums[nums[index]]:
            print(index, nums[index],nums[nums[index]])
            temp = nums[index]
            nums[index] = nums[nums[index]]
            nums[temp] = temp
        if nums[index] == nums[nums[index]]:
            return nums[index]
    return -1

nums = [1, 2, 6, 0, 6, 7, 8, 9, 2, 9, 5]
print(solution(nums))
print(nums)