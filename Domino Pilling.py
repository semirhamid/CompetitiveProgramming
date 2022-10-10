#Algorithm

# 1, set a limit to the input that their value is between 1 and 16
# 2, since the dominos and board are in rectangular shape position won't alter the maximum number
# find the possibility that the board is perfectly hold the dominos and remove the extra one if exists

def domino_pilling(m,n):
    if(1 < m<= 16 and 1 < n <= 16 ):
        max_piece = (m * n) // 2
        return max_piece
    else:
        return -1

m = int(input("Enter the m value: "))
n = int(input("Enter the n value: "))
print(domino_pilling(m, n))
