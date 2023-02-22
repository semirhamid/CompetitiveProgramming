n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = []
curr = 0

for index in range(m):
    while curr < n and arr1[curr] < arr2[index]:
        curr += 1
    result.append(curr)
print(*result)