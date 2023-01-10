class Solution:
    def minIncrementForUnique(self, nums):
        nums.sort()
        left = 0
        right = 1
        count = 0
        while right < len(nums):
            if nums[right]==nums[left]:
                nums[right] += 1
                count += 1
            elif nums[right]<nums[left]:
                diff = (nums[left]-nums[right])+1
                nums[right] += diff
                count += diff
            right += 1
            left += 1

        return count