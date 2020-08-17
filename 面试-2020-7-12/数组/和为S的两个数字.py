"""
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
"""

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        min_resoult = 99999999999
        temp = []
        start = 0
        end = len(array) - 1
        while start < end:
            if tsum == array[start] + array[end]:
                if min_resoult > array[start] * array[end]:
                    min_resoult = array[start] * array[end]
                    temp = [array[start], array[end]]
                start += 1
            elif array[start] + array[end] > tsum:
                end -= 1
            else:
                start += 1
        return temp


array = [1, 2, 4, 7, 8, 11, 15]
tsum = 15
soultion = Solution()
print(soultion.FindNumbersWithSum(array, tsum))