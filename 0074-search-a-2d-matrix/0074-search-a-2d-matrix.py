class Solution:
    def searchMatrix(self, matrix, target): 
        if len(matrix) == 1:
            a =  matrix[0].count(target)
            return a != 0
        left = len(matrix) // 2 
        if target <= matrix[left - 1][-1]:
            return self.searchMatrix(matrix[:len(matrix) // 2 ], target)
        else:
            return self.searchMatrix(matrix[len(matrix) // 2:], target)
        