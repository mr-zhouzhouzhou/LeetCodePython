"""
题目描述
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

"""

"""
如果  

"""

def solution(nums, size):
    temp = []
    result = []
    for index, item in enumerate(nums):
        if len(temp) > 0:
            if index - temp[0] > size - 1:
                temp.pop(0)
            while len(temp) != 0 and item > nums[temp[-1]]:
                temp.pop(-1)
        temp.append(index)
        if index >= size - 1:
            result.append(nums[temp[0]])
    return result

m_list = [2,3,4,2,6,2,5,1]


print(solution(m_list,3))