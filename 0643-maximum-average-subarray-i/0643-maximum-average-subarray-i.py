class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = sum(nums[:k])
        mx = start
        for i in range(k, len(nums)):
            start += nums[i]
            start -= nums[i - k]
            mx = max(mx, start)
        return mx / k