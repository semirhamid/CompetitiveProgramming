class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while low <= high:

            mid = (low + high) // 2
            if high - low + 1 == 1:
                return nums[mid]
            if mid + 1 < len(nums) and nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            if (mid - low + 1) % 2 == 1 and mid + 1 < len(nums):
                if nums[mid] != nums[mid + 1]:
                    high = mid
                else:
                    low = mid
            else:
                if nums[mid] != nums[mid - 1]:
                    high = mid
                else:
                    low = mid + 1