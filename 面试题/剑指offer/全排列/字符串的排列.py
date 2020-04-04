
"""
全排列应该分为2种情况：
1： 有重复的情况
2：没有重复的情况


"""



# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        res = []
        ss = "".join(set(list(ss)))
        self.perm(ss, res, "")
        return res

    def perm(self, ss, res, path):
        if len(ss) == 0:
            res.append(path)
        else:
            for index in range(len(ss)):
                self.perm(ss[:index] + ss[index+1:], res, path+ss[index])

soultion = Solution()
res = soultion.Permutation("aabc")
print(res)
print()