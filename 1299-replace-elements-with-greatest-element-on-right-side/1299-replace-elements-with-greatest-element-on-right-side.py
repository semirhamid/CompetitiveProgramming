class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right = len(arr) - 1
        mx = -1
        while right >= 0:
            temp = arr[right]
            arr[right] = mx
            mx = max(mx, temp)
            right -= 1
        return arr