class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1: return 1
        left = 1
        for right in range(length-1):
            if nums[right] != nums[right + 1]:
                nums[left] = nums[right + 1]
                left += 1
        return  left