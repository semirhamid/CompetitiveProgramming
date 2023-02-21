class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        add = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    add.append([i,j])
        for i , j in add:
            for l in range(row):
                matrix[l][j] = 0
            for k in range(col):
                matrix[i][k] = 0
            