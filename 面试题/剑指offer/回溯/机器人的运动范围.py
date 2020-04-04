

"""
思路：采用回溯法
"""


class Solution:
    def movingCount(self, threshold, rows, cols):
        if rows < 1 or cols < 1:
            return 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        count = [0]
        self.soultion(threshold, rows, cols, 0, 0, visited, count)
        return count[0]

    def soultion(self, threshold, rows, cols, i, j, visited, count):

        if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or self.getCount(i, j) > threshold:
            return False
        visited[i][j] = True
        count[0] = count[0] + 1
        self.soultion(threshold, rows, cols, i + 1, j, visited, count)
        self.soultion(threshold, rows, cols, i - 1, j, visited, count)
        self.soultion(threshold, rows, cols, i, j - 1, visited, count)
        self.soultion(threshold, rows, cols, i, j + 1, visited, count)

    def getCount(self, i, j):
        count = 0
        for item in str(i):
            count = count + int(item)
        for item in str(j):
            count = count + int(item)
        return count




soultion = Solution()
print(soultion.movingCount(15,20,20))