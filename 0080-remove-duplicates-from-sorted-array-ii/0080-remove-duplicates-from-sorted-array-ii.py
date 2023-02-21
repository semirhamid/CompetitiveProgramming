class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2: return length
        slow = 2
        for fast in range(2, length):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
        return slow