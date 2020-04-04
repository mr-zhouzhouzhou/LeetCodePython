#  打印从 1 到最大的 n 位数
"""

"""

def solution(n):
    if n <= 0:
        return
    nums = [-1]*n
    print1ToN(nums, 0)

def print1ToN(nums, digit):
    if digit == len(nums):
        print(nums)
        return
    for i in range(10):
        nums[digit] = i
        print1ToN(nums, digit + 1)

solution(2)