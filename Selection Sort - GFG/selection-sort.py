class Solution: 
    def select(self, arr, i):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        return min_index


    def selectionSort(self,arr, n):
        # code here
        for i in range(n - 1):
            index = self.select(arr, i )
            arr[i], arr[index] = arr[index], arr[i]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
