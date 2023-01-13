class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            dic = {}
            for j in row:
                if j in dic and j != ".":
                    return False
                dic[j] = 1
        
        for col in range(len(board[0])):
            dic = {}
            for k in range(len(board)):
                if board[k][col] in dic and board[k][col] != ".":
                    return False
                dic[board[k][col]] = 1
        idx = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        for m , n in idx:
            dic = {}
            for k in range(3):
                for l in range(3):
                    if board[m + k][n + l] in dic and board[m + k][n + l] != ".":
                        return False
                    dic[board[m + k][n + l]] = 1 
        return True
