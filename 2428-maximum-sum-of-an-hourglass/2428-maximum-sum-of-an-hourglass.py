class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        col = len(grid)
        row = len(grid[0])

        new_matrix = [[0] * (row + 1) for i in range(col + 1)]
        for i in range(col):
            prefix = 0
            for j in range(row):
                prefix += grid[i][j]
                new_matrix[i + 1][j + 1] = new_matrix[i][j + 1] + prefix
        new_col = len(new_matrix)
        new_row = len(new_matrix[0])
        mx = sm = 0

        for i in range(3, new_col):
            for j in range(3, new_row):
                other = 0
                sm = new_matrix[i][j]
                left = grid[i - 2][j - 3]
                right = grid[i - 2][j - 1]
                lower = new_matrix[i - 3][j]
                upper = new_matrix[i][j - 3]
                other = new_matrix[i-3][j-3]
                sm = sm - left - right - lower - upper + other
                mx = max(sm, mx)
        return mx
