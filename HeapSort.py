class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        largest = i
        left = 2 * i+1
        right = 2 * i+2
        
        if left < n and arr[i] < arr[left]:
            largest = left
            
        if right < n and arr[largest] < arr[right]:
            largest = right
            
        if i != largest:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        j = (n-1)//2
        for i in range(j, -1, -1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)
