"""

题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。
序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序。
"""
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum <= 1:
            return []
        cont_list = []
        temp = 0
        count = 0
        temp_list = []
        while True:
            if temp >= (tsum+3)/2:
                    return cont_list
            if count == tsum:
                temp_a = [item for item in temp_list]
                cont_list.append(temp_a)
                a = temp_list.pop(0)
                count = count - a
            elif count < tsum:
                temp = temp + 1
                count = count + temp
                temp_list.append(temp)
            else:
                a = temp_list.pop(0)
                count = count - a

solution = Solution()
temp_list = solution.FindContinuousSequence(9)

print(temp_list)

for item in temp_list:
    print(item)