class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        mn = nums[k - 1] - nums[left]
        for right in range(k, len(nums)):
            left += 1
            mn = min(mn, nums[right] - nums[left])

        return mn