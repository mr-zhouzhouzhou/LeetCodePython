


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) < 2:
            return []
        low = 0
        high = target - 1
        while low < target:

            temp = nums[low] + nums[high]
            if temp == target:
                return [low, target]
            elif temp < target:
                low += 1
            else:
                high -= 1

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m_dict = {}
        for index, item in enumerate(nums):
            if m_dict.get(target - item) is not None:
                return [m_dict[target - item], index]
            else:
                m_dict[item] = index
        return []