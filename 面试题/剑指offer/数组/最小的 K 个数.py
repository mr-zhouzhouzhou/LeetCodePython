


"""
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
"""

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput is None or k <= 0 or len(tinput) < k:
            return []
        start = 0
        end = len(tinput) - 1
        self.quick(tinput, start, end, k)
        resoult = tinput[:k]
        resoult.sort()
        return resoult

    def quick(self, nums, low, high, k):
        if low < high:
            pi = self.partition(nums, low, high)
            if pi == k:
                return
            elif pi > k:
                self.quick(nums, low, pi - 1, k)
            else:
                self.quick(nums, pi + 1, high, k)

    def partition(self, nums, low, high):
        i = low - 1
        piv = nums[high]
        for j in range(low, high):
            if nums[j] <= piv:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        nums[i+1], nums[high] = nums[high], nums[i + 1]
        return i + 1

def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)



# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

nums = [4, 5, 1, 6, 9, 7, 3, 8]
soultion = Solution()
pi = soultion.GetLeastNumbers_Solution(nums, 8)

print(pi)
