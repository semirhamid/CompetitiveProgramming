length = int(input())
arr = list(map(int, input().split()))
flag = False
flag1 = False
for i in arr:
    if i % 2== 1:
        flag = True
for i in arr:
    if i % 2== 0:
        flag1 = True
if flag and flag1:
    arr.sort()
    print(*arr)
else:
    print(*arr)
