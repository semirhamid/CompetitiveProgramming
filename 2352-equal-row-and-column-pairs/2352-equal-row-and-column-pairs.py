class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_dic = {}
        col_dic = {}
        for i in grid:
            word = ""
            for j in i:
                word += str(j) + "-"
            row_dic[word] = row_dic.get(word,0) + 1

        for i in range(len(grid)):
            word = ""
            for j in range(len(grid)):
                word += str(grid[j][i]) + "-"
            col_dic[word] = col_dic.get(word, 0) + 1
        count = 0
        res = {}
        for i in row_dic:
            if i in col_dic:
                count += row_dic[i] * col_dic[i]
        return count