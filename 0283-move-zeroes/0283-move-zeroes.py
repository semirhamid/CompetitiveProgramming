class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        length = len(nums)

        while length > 1 and right < length:
            if nums[left] == 0:
                while right < (length- 1) and nums[right] == 0:
                    right += 1
                nums[left], nums[right] = nums[right], nums[left]
            right += 1
            left += 1

            
        