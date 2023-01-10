class Solution:
    def divisorSubstrings(self, nums: int, k: int) -> int:
        ori = nums
        nums = str(nums)
        count = 0
        for i in range(len(nums)-k + 1):
            temp = int(nums[i:i + k])
            if temp != 0 and ori % temp == 0:
                count += 1
        return count