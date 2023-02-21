n , m = map(int,input().split())
result = ""
grid = []
for  i in range(n):
    grid.append(list(input()))

for i in range(n):
    for j in range(m):
        flag = True
        for k in range(n):
            if k != i and grid[k][j] == grid[i][j]:
                flag = False
        for l in range(m):
            if l != j and grid[i][l] == grid[i][j]:
                flag = False
        if flag:
            result+= grid[i][j]
print(result)
        