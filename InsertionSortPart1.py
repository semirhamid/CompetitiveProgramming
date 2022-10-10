#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

#Algorithm
# store the last element in a variable key
# track the current index starting from the last element to first 
# while the current index is greater than zero and the below element greater than or equals to the key
# insert the below element to the current index position and print the array
# finally insert the key to the current element and print the array

def insertionSort1(n, arr):
    key = arr[n-1]
    current_index = n-1
    
    while current_index > 0 and arr[current_index-1] >= key:
        arr[current_index] = arr[current_index - 1]
        current_index -= 1
        print(*arr)
        
    arr[current_index] = key
    print(*arr)

insertionSort1(5,[1,2,4,5,3])

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
