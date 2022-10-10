# Algorithm
# declare a variable to track the number of swaps
# iterate through the array
# if adjacent element less than the previous one bubble the element to the next
# count if the element get swapped


def countSwaps(a):
    swap_count = 0
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j],a[j+1] = a[j+1], a[j]
                swap_count += 1
    print("a is sorted in", swap_count, "swaps.")
    print('First Element:', a[0])
    print("Last Element:", a[-1])
    return a

print(countSwaps([9,8,7,6,5,4,3,2,1]))
