class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        l, ans = 0, -1
        total = 0
        
        target = sum(nums) - x
        if target < 0:
            return -1
        
        for r, val in enumerate(nums):
            total += val
            while total > target:
                total -= nums[l]
                l += 1
            if total == target:
                ans = max(ans, r - l + 1)
        return -1 if ans == -1 else len(nums) - ans