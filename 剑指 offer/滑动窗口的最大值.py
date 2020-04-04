"""
题目描述
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

"""

# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self,num, size):
        if size == 0 or len(num) == 0:
            return []
        q = []  # 用来存放最大值的队列(存放的不是值，是该值对应的num索引)
        result = []
        for i in range(len(num)):
            print('current q',q)
            if len(q) > 0:
                #先剔除超出窗口的元素
                if (i - q[0]) > (size-1):
                    q.pop(0)
                #如果当前元素比队尾元素要大，剔除队尾元素
                while len(q) > 0 and num[i] >= num[q[-1]]:
                    q.pop(-1)
            #每个元素只执行了一次的入队操作，所以复杂度是O(n)
            q.append(i)
            #应对刚开始遍历元素不足size数量的情况。
            if i >= size-1:
                result.append(num[q[0]])
        return result


m_list = [2,3,4,2,6,2,5,1]

solution = Solution()
print(solution.maxInWindows(m_list, 3))

