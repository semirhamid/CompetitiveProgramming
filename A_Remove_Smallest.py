test_cases = int(input())
for _ in range(test_cases):
    length = int(input())
    arr = list(map(int, input().split()))
    count = 0
    arr.sort()
    left = 0
    for right in range(length - 1):
        if abs(arr[right] - arr[right + 1]) > 1:
            count += 1
    if count == 0: print("YES") 
    else: print("NO")