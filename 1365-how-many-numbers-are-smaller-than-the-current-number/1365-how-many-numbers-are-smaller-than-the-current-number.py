class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_arr = [0] * len(nums)
        for i in range(len(new_arr)):
            count = 0
            for j in range(len(new_arr)):
                if nums[j] < nums[i] and j != i:
                    count += 1
            new_arr[i] = count
        return new_arr