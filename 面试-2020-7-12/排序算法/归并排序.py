


def mergeSort(nums, low, high, resoult, count):
    if low >= high:
        return
    middle = (low + high) // 2
    mergeSort(nums, low, middle, resoult, count)
    mergeSort(nums, middle + 1, high, resoult, count)
    sort(nums, low, high, resoult, count)


def sort(nums, low, high, resoult, count):
    if low >= high:
        return
    middle = (low + high) // 2
    nums_a_flag = middle
    nums_b_flag = high
    resoult_flag = high
    while nums_a_flag >= low and nums_b_flag > middle:
        if nums[nums_a_flag] >= nums[nums_b_flag]:
            resoult[resoult_flag] = nums[nums_a_flag]
            resoult_flag -= 1
            nums_a_flag -= 1
            length = nums_b_flag - middle
            temp_b_flag = nums_b_flag
            while nums[temp_b_flag] == nums[nums_a_flag]:
                length -= 1
                temp_b_flag -= 1
            count[0] += length
        else:
            resoult[resoult_flag] = nums[nums_b_flag]
            resoult_flag -= 1
            nums_b_flag -= 1
    if nums_a_flag >= low:
        resoult[resoult_flag] = nums[nums_a_flag]
        resoult_flag -= 1
        nums_a_flag -= 1
    if nums_b_flag > middle:
        resoult[resoult_flag] = nums[nums_b_flag]
        resoult_flag -= 1
        nums_b_flag -= 1
    while high >= low:
        nums[high] = resoult[high]
        high -= 1

nums = [1,2,3,4,5, 6, 7, 0]
a = 0
b = len(nums) - 1
resoult = [0] * len(nums)
count = [0]
print(nums)
mergeSort(nums, a, b, resoult, count)
print(count[0])