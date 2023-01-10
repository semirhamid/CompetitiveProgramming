class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        count = sys.maxsize
        prefix_sum = 0
        for right in range(len(nums)):
            prefix_sum += nums[right]
            while prefix_sum - nums[left] >= target:
                prefix_sum -= nums[left]
                left += 1
            if prefix_sum >= target:
                count = min(count, (right - left) +1)

        return 0 if count == sys.maxsize else count