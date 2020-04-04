




"""
时间复杂度是O(n), 空间复杂度是O(1)

"""
def soultion(nums):
    if nums is None or len(nums) <= 1:
        return -1
    for index, item in enumerate(nums):
         while nums[index] != index:
             if nums[index] == nums[nums[index]]:
                 return nums[index]
             else:
                 swap(nums, index, nums[index])
    return -1

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

nums = [2, 3, 1, 0, 2, 5]
resoult = soultion(nums)
print(resoult)