"""
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
输入描述:
题目保证输入的数组中没有的相同的数字

数据范围：

	对于%50的数据,size<=10^4

	对于%75的数据,size<=10^5

	对于%100的数据,size<=2*10^5


	1,2,3,4,5,6,7,0

	7
"""
class Solution:
    def __init__(self):
        self.count = 0
        self.tmp = None
    def InversePairs(self, data):
        self.tmp = [0] * len(data)
        self.mergeSort(data, 0, len(data)-1)
        return self.count
    def mergeSort(self, data, low, high):
        if low == high:
            return
        middle = (low + high) // 2
        self.mergeSort(data, low, middle)
        self.mergeSort(data, middle + 1, high)
        self.merge(data, low, middle, high)
        return self.count

    def merge(self, data, low, middle, high):
        left_data = [data[index] for index in range(low, middle+1)]
        right_data = [data[index] for index in range(middle+1, high+1)]
        left_index = 0
        right_index = 0
        data_index = low
        length = 0
        while left_index < len(left_data) and right_index < len(right_data):
            if left_data[left_index] < right_data[right_index]:
                data[data_index] = left_data[left_index]
                flag = 0
                while left_data[left_index] > right_data[flag]:
                    flag += 1
                    length += 1
                    if flag >= len(right_data):
                        break
                data_index += 1
                left_index += 1
            else:
                data[data_index] = right_data[right_index]

                data_index += 1
                right_index += 1

        while left_index < len(left_data):
            data[data_index] = left_data[left_index]
            flag = 0
            while left_data[left_index] > right_data[flag]:
                flag += 1
                length += 1
                if flag >= len(right_data):
                    break
            data_index += 1
            left_index += 1
        while right_index < len(right_data):
            data[data_index] = right_data[right_index]
            data_index += 1
            right_index += 1
        self.count += length



data = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
#data = [1,2,3,4,5,6,7,0]
#data = [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601]
sSolution = Solution()
length = sSolution.InversePairs(data)




#
# # -*- coding:utf-8 -*-
# class Solution:
#     def __init__(self):
#         self.count = 0
#     def InversePairs(self, data):
#         low = 0
#         high = len(data) - 1
#         temp = [0] * len(data)
#         count = [0]
#         self.mergerSort(data, low, high, temp, count)
#
#     def mergerSort(self,data, low, high, temp, count):
#         if low >= high:
#             return
#         middle = (low + high) // 2
#         self.mergerSort(data, low, middle, temp, count)
#         self.mergerSort(data, middle + 1, high, temp, count)
#         self.sort(data, low, middle, high, temp, count)
#
#
#     def sort(self, data, low, middle, high, temp, count):
#
#         if low >= high:
#             return
#         index_a = middle
#         index_b = high
#         index_temp = high
#         # print("##################")
#         # print(low,middle)
#         #
#         # print(data[low:middle+1])
#         # print(middle+1, high)
#         # print(data[middle+1:high+1])
#         # print("#")
#         while index_a >= low and index_b > middle:
#             if data[index_a] >= data[index_b]:
#                 temp[index_temp] = data[index_a]
#                 length = index_b - middle
#                 flag = index_b
#                 while data[flag] == data[index_a]:
#                     length -= 1
#                     flag -= 1
#                 self.count += length
#
#                 index_a -= 1
#                 index_temp -= 1
#             else:
#                 temp[index_temp] = data[index_b]
#                 index_b -= 1
#                 index_temp -= 1
#         if index_a >= low:
#             temp[index_temp] = data[index_a]
#             index_temp -= 1
#             index_a -= 1
#         if index_b > middle:
#             temp[index_temp] = data[index_b]
#             index_b -= 1
#             index_temp -= 1
#         for index in range(low, high+1):
#             data[index] = temp[index]




# import sys
# n = map(int, sys.stdin.readline().strip().split())
#
# for item in n:
#
#     print(item)
#
#
# hangshu = 3
# a,b,c=[int(i) for i in input().split()]
# list=[]
# for i in range(hangshu):
#     list.append([int(i) for i in input().split()])
#     print(list)
#
# a,b,c=[int(i) for i in input().split()]
# list=[]
# for i in range(hangshu):
#     list.extend([int(i) for i in input().split()])
#     print(list)
#
# def convert():
#     res = ""
#     str = input()
#     str = str.lower()
#     if str[0].isalnum():
#         str = str
#     else:
#         str = str[1:]
#     flag = 0
#     for i in range(0, len(str)):
#         if str[i].isalnum():
#             if flag == 0:
#                 res+= str[i]
#             else:
#                 res += str[i].upper()
#                 flag = 0
#         else:
#             if i+1 < len(str):
#                 flag = 1
#     print(res)
# convert()
#
#
def findNext(nums):
    if len(nums) == 1:
        return nums
    right = len(nums) - 1
    left = right - 1
    hasBigger = False
    while left >= 0:
        if nums[right] < nums[left]:
            k = right + 1
            hasBigger = True
            while k < len(nums):
                if nums[k] >= nums[left]:
                    break
            nums[k - 1], nums[left] = nums[left], nums[k-1]
            left += 1
        right -= 1
        left -= 1
    if not hasBigger:
        left = 0
    leftPart = nums[:left]
    rightPart = nums[left:]
    rightPart.sort()
    return leftPart+rightPart

def solution(number):
    numsStr = str(number)
    nums = list(numsStr)
    resultList = findNext(nums)
    result = "".join(resultList)
    return int(result)




def f(num):
    nums = list(str(num))
    length = len(nums) - 1
    Flag = False
    for index in range(length, 0, -1):
        if nums[index] < nums[index-1]:
            Flag = True
            nums[index], nums[index-1] = nums[index-1], nums[index]
            break
    if Flag:
        return int("".join(nums))
    else:
        return 0



print(f(0))