




tmp = []
cnt = 0

def inversePairs(nums):
    tmp = []
    cnt = []
    mergeSort(nums, 0, len(nums) - 1, tmp, cnt)
    return cnt[0]


def mergeSort(nums, l, h, tmp, cnt):
    if h - l < 1:
        return
    m = l + (h - l)//2
    mergeSort(nums, l, m, tmp, cnt)
    mergeSort(nums, m + 1, h, tmp, cnt)
    merge(nums, l, m, h, tmp, cnt)


def merge(nums, l, m, h, tmp, cnt):
    i = l
    j = m + 1
    k = l
    while i <= m or j <=h:
        if i > m:
            tmp[k] = nums[j]
            j += 1
        elif j > h:
            tmp[k] = nums[i]
            i += 1
        elif nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
            cnt[0] += m - i + 1
        k += 1
    for index in range(l, h):
        nums[index] = tmp[index]




