

class Solution:
    def reOrderArray(self, array):
        # write code here
        start = 0
        end = len(array) - 1
        while start < end:
            while start < end and array[start] % 2 != 0:
                start += 1
            while start < end and array[end] % 2 == 0:
                end -= 1
            self.swap(array, start, end)
        return array
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


nums = [1,2,3,4,5,6,7,8,9]
solution = Solution()
print(solution.reOrderArray(nums))