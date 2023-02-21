length , k = list(map(int,input().split()))
arr = list(map(int, input().split()))
arr.sort()
if k == 0:
    print(arr[0] - 1)
elif k >= length:
    print(arr[-1] + 1)
else:
    if arr[k - 1] == arr[k]:
        print(-1)
    else:
        print(arr[k-1] + 1)
        
        