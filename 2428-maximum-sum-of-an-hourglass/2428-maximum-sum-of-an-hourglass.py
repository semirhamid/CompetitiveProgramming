class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        ans = 0
        cols = len(grid[0])
        rows = len(grid)
        for i in range(1, rows-1):
            for j in range(1, cols-1):

                sm = ( grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
                                      + grid[i  ][j] +
                       grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1] )

                ans = max(ans, sm)

        return ans