


class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])

        dp = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(col):
            if i == 0:
                dp[0][i] = grid[0][i]
            else:
                dp[0][i] = grid[0][i] + dp[0][i - 1]

        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = max(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])
        return dp[row-1][col-1]
