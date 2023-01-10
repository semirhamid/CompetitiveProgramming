class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(arr)-1
        right = length

        while right > 0 and arr[right -1] >= arr[right]:
            right -=1
        if right == 0:
            self.reverse(0,arr)
            return
        nx = right
        while nx < length and arr[nx + 1] > arr[right -1] :
            nx += 1
        arr[nx],arr[right-1] = arr[right - 1], arr[nx]
        self.reverse(right, arr)
        return arr

    def reverse(self,right, arr):
        left = right
        right = len(arr)-1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        