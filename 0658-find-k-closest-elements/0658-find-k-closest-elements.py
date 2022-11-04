class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(nums) - k 
        while left < right:
            m = (left + right) // 2
            if x - nums[m] > nums[m + k] - x:
                left = m + 1
            else:
                right = m
        return nums[left : left + k]