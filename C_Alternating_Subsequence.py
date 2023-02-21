test_cases = int(input())
for _ in range(test_cases):
    length = int(input())
    arr = list(map(int, input().split()))
    stack = [arr[0]]
    for right in range(1, length):
        if stack[-1] < 0 and arr[right] < 0:
            stack[-1] = max(stack[-1], arr[right])
        elif stack[-1] < 0  and arr[right] > 0:
            stack.append(arr[right])
        elif stack[-1] > 0 and arr[right] > 0:
            stack[-1] = max(stack[-1], arr[right])
        elif stack[-1] > 0 and arr[right] < 0:
            stack.append(arr[right])
    print(sum(stack))