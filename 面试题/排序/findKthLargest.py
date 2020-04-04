

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) < k:
            return None
        k = len(nums) - k
        start = 0
        end = len(nums) - 1
        while start < end:
            pi = self.parition(nums, start, end)
            if pi == k:
                return nums[k]
            elif pi > k:
                end = pi - 1
            else:
                start = pi + 1



    def parition(self, nums, start, end):
        i = start - 1
        pi = nums[end]
        for index in range(start, end + 1):
            if nums[index] <= pi:
                i += 1
                nums[i], nums[index] = nums[index], nums[i]
        nums[i + 1], nums[end] = nums[end], nums[i + 1]
        return i + 1

nums = [3,2,1,5,6,4]
k = 2

solution = Solution()
print(solution.findKthLargest(nums, k))