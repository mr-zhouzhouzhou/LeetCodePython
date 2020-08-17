"""
题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如
[ [a、b、c、e]
  [s、f、c、s】
  [a、d、e、e] ]
矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""

# #

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        temp  = [[matrix[row*cols + col ] for col in range(cols)] for row in range(rows)]
        matrix = temp
        for x in range(rows):
            for y in range(cols):
                flag = self.checkPath(matrix, rows, cols, path, x, y, visited, 0)
                if flag:
                    return True
        return False

    def checkPath(self, matrix, rows, cols, path, x, y, visited, pathIndex):
        if pathIndex >= len(path):
            return True
        if x < 0 or y < 0 or x >= rows or y >= cols or pathIndex >= len(path):
            return False
        if path[pathIndex] != matrix[x][y]:
            return False
        visited[x][y] = True
        flag = self.checkPath(matrix, rows, cols, path, x - 1, y, visited, pathIndex + 1) or \
               self.checkPath(matrix, rows, cols, path, x + 1, y, visited, pathIndex + 1) or \
               self.checkPath(matrix, rows, cols, path, x, y - 1, visited, pathIndex + 1) or \
               self.checkPath(matrix, rows, cols, path, x, y + 1, visited, pathIndex + 1)
        if flag is False:
            visited[x][y] = False
            return False
        else:
            return True

solution = Solution()

#matrix = ["a", "s", "a", "b", "f", "d", "c", "c", "e", "e", "s", "e"]​
matrix = ["A", "B", "C", "E", "S", "F", "C", "S", "A", "D", "E", "E"]
#matrix = [["a", "b", "c", "e"],["s", "f", "c", "s"],["a", "d", "e", "e"]]
rows = 3
cols = 4
path = "ABCB"
#ABCCED
#ABCESFCSADEE
resoult = solution.hasPath(matrix, rows, cols, path)
#resoult = solution.hasPath("ABCESFCSADEE", 3, 4, "ABCB")
print(resoult)


#ABCESFCSADEE