class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)

        if k > 0 and k != length:
            self.rotator(0,length-1, nums)
            self.rotator(0,(k-1)%length,nums)
            self.rotator(k%length ,length-1, nums)


    def rotator(self,left, right, arr):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
            left += 1