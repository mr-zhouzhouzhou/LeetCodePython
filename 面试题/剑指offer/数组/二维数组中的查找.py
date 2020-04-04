
"""
给定一个二维数组，其每一行从左到右递增排序，
从上到下也是递增排序。给定一个数，判断这个数是否在该二维数
组中。
"""


def soultion(nums, target):
    if nums is None or len(nums) == 0:
        return False
    rows = len(nums)
    cols = len(nums[0])
    row_temp = rows - 1
    cols_temp = 0
    while row_temp >= 0 and cols_temp < cols:
        temp = nums[row_temp][cols_temp]
        if temp == target:
            return True
        elif temp > target:
            row_temp = row_temp - 1
        else:
            cols_temp = cols_temp + 1
    return False


nums = [[1, 4, 7, 11,15],
         [2, 5, 8, 12, 19],
         [3, 6, 9, 16, 22],
         [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 30]]

print(soultion(nums, 29))