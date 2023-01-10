class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums) - 1
        new = [1] * len(nums)
        for i in range(len(nums)):
            if nums[i]==2:
                new[end] = 2
                end -=1
            elif nums[i]==0:
                new[start] = 0
                start +=1
        nums[:] = new
        