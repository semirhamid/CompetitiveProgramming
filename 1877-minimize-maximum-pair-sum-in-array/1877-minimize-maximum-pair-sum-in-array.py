class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = []
        size = len(nums)
        for i in range(size):
            start = i
            end = (size - 1) - i
            result.append(nums[start] + nums[end])
        return max(result)