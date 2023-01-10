class Solution:
    def findTheWinner(self, nums: int, k: int) -> int:
        arr = [i for i in range(1,nums+1)]
        right = 0
        while len(arr) >1:
            r = (right + (k-1))% len(arr)
            right = r
            del arr[r]
        return arr[0]