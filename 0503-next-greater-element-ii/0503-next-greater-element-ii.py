class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums += nums
        mono = []
        result = [0]*len(nums)
        for i in range(len(nums) - 1, -1 ,-1):
            while mono and nums[i] >= mono[-1]:
                mono.pop()
            result[i] = (-1 if len(mono) == 0 else mono[-1])
            mono.append(nums[i])

        return result[:len(nums)//2]
