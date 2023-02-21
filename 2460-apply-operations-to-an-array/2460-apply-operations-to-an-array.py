class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        left= 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
                
        for i in range(left, len(nums)):
            nums[i] = 0
        return nums
            