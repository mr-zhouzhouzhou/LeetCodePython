



# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum <= 1:
            return []
        visited = []
        count = 0
        resoult = []
        for index in range(1, tsum//2 + 2):
            count += index
            visited.append(index)
            if count > tsum:
                while count > tsum:
                    count -= visited[0]
                    visited.pop(0)
                    print(visited)
                if count == tsum:
                    resoult.append([item for item in visited])
            elif count == tsum:
                resoult.append([item for item in visited])
        return resoult

solution =Solution()
print(solution.FindContinuousSequence(100))
