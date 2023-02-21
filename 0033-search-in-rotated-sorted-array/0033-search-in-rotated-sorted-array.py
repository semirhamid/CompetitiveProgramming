class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return nums.index(nums[i])
                break
        else:
            return -1