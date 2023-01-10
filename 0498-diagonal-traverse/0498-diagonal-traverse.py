class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        r_max = len(mat[0]) - 1
        c_max = len(mat) - 1
        for i in range(len(mat) + len(mat[0]) - 1):
            temp = []
            right = min(i, r_max)
            left = i - right
            while left + right == i and left <= c_max and right <= r_max and left >= 0 and right >= 0:
                temp.append(mat[left][right])
                right -= 1
                left  = i - right
            if i % 2 == 0:
                temp = temp[::-1]
            for i in temp:
                result.append(i)
                
        return result
