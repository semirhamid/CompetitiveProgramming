class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        cols = {i: 0 for i in range(len(grid[0]))}
        rows = {i: 0 for i in range(len(grid))}
        
        for i in range(len(grid)):
            rows[i] = grid[i].count(1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cols[j] += 1
        row_len = len(grid[0])
        col_len = len(grid)
                    
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(rows[i] + cols[j] -  (row_len - rows[i] ) - (col_len - cols[j]))
            result.append(temp)
        return result
            