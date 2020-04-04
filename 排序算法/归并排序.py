def mergeSort(nums, low, high, tmp):
    if low >= high:
        return
    middle = (low + high) // 2
    mergeSort(nums, low, middle, tmp)
    mergeSort(nums, middle + 1, high, tmp)
    merge(nums, low, middle, high, tmp)

def merge(nums, low, middle, high, tmp):
    i = low
    j = middle + 1
    k = low
    while i <= middle or j <= high:
        if i > middle:

            tmp[k] = nums[j]
            j += 1
        elif j > high:
            tmp[k] = nums[i]
            i += 1
        elif nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1
    for index in range(low, high + 1):
        nums[index] = tmp[index]

nums = [1, 3, 7, 2, 8, 4, 99, 6]
low = 0
high = len(nums) - 1
tmp = [0] * len(nums)
mergeSort(nums, low, high, tmp)
print(nums)