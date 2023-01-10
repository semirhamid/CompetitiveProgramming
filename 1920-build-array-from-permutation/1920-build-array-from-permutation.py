class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = [None] * len(nums)
        for i in range(len(nums)):
            result[i] = nums[nums[i]]
        return result