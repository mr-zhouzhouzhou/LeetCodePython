



"""
思路：

"""

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if rows == 0 or cols == 0 or len(path) == 0 or len(matrix) != cols * rows:
            return False

        visited = [False] * len(matrix)

        for i in range(rows):
            for j in range(cols):
                flag = self.haspath(matrix,  rows, cols, i, j, path, visited, 0)
                if flag:
                    return flag
        return False

    def haspath(self, matrix,  rows, cols, row, col, path, visited, pathindex):
        if pathindex >= len(path):
            return True
        index = row * cols + col
        if row < 0 or row >= rows or col < 0 or col >= cols or visited[index] or matrix[index] != path[pathindex]:
            return False
        visited[index] = True
        flag = self.haspath(matrix,  rows, cols, row - 1, col, path, visited, pathindex+1) or \
               self.haspath(matrix,  rows, cols, row + 1, col, path, visited, pathindex+1) or \
               self.haspath(matrix,  rows, cols, row, col - 1, path, visited, pathindex+1) or \
               self.haspath(matrix,  rows, cols, row, col + 1, path, visited, pathindex+1)

        if flag is False:
            visited[index] = False
        return flag


solution = Solution()

#matrix = ["a", "s", "a", "b", "f", "d", "c", "c", "e", "e", "s", "e"]​
matrix = ["a", "s", "a", "b", "f", "d", "c", "c", "e", "e", "s", "e"]
rows = 3
cols = 4
path = "bcced"
resoult = solution.hasPath(matrix, rows, cols, path)
#resoult = solution.hasPath("ABCESFCSADEE", 3, 4, "ABCB")
print(resoult)



