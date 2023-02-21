class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1
        spiral_arr = []
        while left <= right and top <= bottom:
            #  first row left to right
            for col in range(left,right+1):
                spiral_arr.append(matrix[top][col])
            top += 1
            #  last row left to right
            for row in range(top, bottom+1):
                spiral_arr.append(matrix[row][right])
            right -= 1
            #  last row right to left
            for col in range(right, left-1, -1):
                spiral_arr.append(matrix[bottom][col])
            bottom -= 1
             # left bottom to top left
            for row in range(bottom, top-1, -1):
                spiral_arr.append(matrix[row][left])
            left += 1
        return spiral_arr[:m*n]