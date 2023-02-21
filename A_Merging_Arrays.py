l1, l2 = list(map(int, input().split()))
left = 0
right = 0
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = []
while left < l1 and right < l2:
    if arr1[left] < arr2[right]:
        
        arr3.append(arr1[left])
        left += 1
    else:
        
        arr3.append(arr2[right])
        right += 1
if left < l1:
    arr3.extend(arr1[left:])
if right < l2:
    arr3.extend(arr2[right:])
    
print(*arr3)