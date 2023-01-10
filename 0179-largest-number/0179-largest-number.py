class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        result = ""
        for step in range(1, len(nums)):
            key = nums[step]
            j = step - 1
            while j >= 0 and str(key) + str(nums[j]) > str(nums[j]) + str(key):
                nums[j + 1] = nums[j]
                j = j - 1
            nums[j + 1] = key

        if nums[0]==0:
            return "0"
        else:
            return "".join(str(n) for n in nums)