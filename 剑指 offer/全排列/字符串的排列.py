"""
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""


# def perm(ss, res, path):
#     if ss == '':
#         res.append(path)
#     else:
#         for i in range(len(ss)):
#             perm(ss[:i] + ss[i + 1:], res, path + ss[i])
#
#
# ss = "abcd"
# res = []
#
# path = ""
# perm(ss, res, path)
#
# print(res)


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pass


def pern(nums, res, path):
    if len(nums) == 0:
        if path not in res:
            res.append(path)
    else:
        for index in range(len(nums)):
            temp = [item for item in path]
            temp.append(nums[index])
            pern(nums[:index]+nums[index+1:], res, temp)


nums = ["a", "b", "c"]
res = []
path = []


pern(nums, res, path)
print(res)

