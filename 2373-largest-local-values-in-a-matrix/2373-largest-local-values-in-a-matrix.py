class Solution:
    def largestLocal(self, grid):
        result = []
        for i in range(1, len(grid) - 1):
            current = []
            for j in range(1, len(grid[0]) - 1 ):
                temp = [grid[i - 1][j-1],  grid[i - 1][j ], grid[i - 1][j + 1],grid[i ][j - 1], grid[i ][j ], grid[i][j + 1], grid[i + 1][j - 1],grid[i + 1][j], grid[i + 1][j + 1]]
                current.append(max(temp))
            result.append(current)
        return result