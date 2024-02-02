# 64. Minimum path sum
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dynamic programming
        m = len(grid)
        n = len(grid[0])
        # first row
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        # gradually growing column
        for j in range(1, m):
            grid[j][0] += grid[j-1][0]
            # filling the rest row and column
            for k in range(1, n):
                grid[j][k] += min(grid[j-1][k], grid[j][k-1])
        return grid[m-1][n-1]