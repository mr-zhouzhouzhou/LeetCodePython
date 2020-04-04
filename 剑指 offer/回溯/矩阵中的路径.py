"""

"""
# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if len(matrix) == 0 or len(path) == 0 or len(matrix) != rows * cols:
            return False
        visited = [False] * len(matrix)
        for index_i in range(rows):
            for index_j in range(cols):
                flag = self.haspath(matrix, rows, cols, path, index_i, index_j, visited, 0)
                if flag:
                    return flag
        return False

    def haspath(self, matrix, rows, cols, path, i, j, visited, pathlength):
        if pathlength >= len(path):
            return True
        index = cols * i + j
        if i < 0 or i >= rows or j < 0 or j >= cols or visited[index] or  path[pathlength] != matrix[index]:
            return False
        visited[index] = True
        flag = self.haspath(matrix, rows, cols, path, i - 1, j, visited, pathlength + 1) or\
               self.haspath(matrix, rows, cols, path, i, j - 1, visited, pathlength + 1) or\
               self.haspath(matrix, rows, cols, path, i + 1, j, visited, pathlength + 1) or\
               self.haspath(matrix, rows, cols, path, i, j + 1, visited, pathlength + 1)
        if flag is False:
            visited[index] = False
            return False
        else:
            return True

solution = Solution()

#matrix = ["a", "s", "a", "b", "f", "d", "c", "c", "e", "e", "s", "e"]​
matrix = ["a", "s", "a", "b", "f", "d", "c", "c", "e", "e", "s", "e"]
rows = 3
cols = 4
path = "bcced"
resoult = solution.hasPath(matrix, rows, cols, path)
#resoult = solution.hasPath("ABCESFCSADEE", 3, 4, "ABCB")
print(resoult)
