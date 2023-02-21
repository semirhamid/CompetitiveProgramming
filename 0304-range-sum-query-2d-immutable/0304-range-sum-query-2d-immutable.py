class NumMatrix:

    def __init__(self, matrix):
        ROWS = len(matrix) # this is to avoid edge cases
        COLS = len(matrix[0])
        self.offMatrix = [[0] * (COLS + 1) for i in range((ROWS + 1))]

        for i in range(ROWS):
            linear_prefix = 0
            for j in range(COLS):
                linear_prefix += matrix[i][j]
                self.offMatrix[i + 1][j + 1] = self.offMatrix[i][j + 1] + linear_prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
        # increase rows and column by 1 since we added extra column and row
        row1, row2, col2, col1 = row1 + 1, row2 + 1, col2 + 1, col1 + 1
        return self.offMatrix[row2][col2] - self.offMatrix[row2][col1 - 1] - self.offMatrix[row1 - 1][col2] + self.offMatrix[row1 - 1][col1 - 1]
