class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        size = len(nums)
        for i in range(size):
            start = i
            end = (size - 1) - i
            result= max(result, nums[start] + nums[end])
        return result