class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        range_array = [[0] * (n + 1) for i in range(n + 1)]
        for r1, c1, r2, c2 in queries:
            for i in range(r1, r2 + 1):
                range_array[i][c1] += 1
                range_array[i][c2 + 1] -= 1
        for i in range(n + 1):
            for j in range(1, n + 1):
                range_array[i][j] += range_array[i][j - 1] 
        result = []
        for row in range_array:
            result.append(row[: -1])
        result.pop()
        return result