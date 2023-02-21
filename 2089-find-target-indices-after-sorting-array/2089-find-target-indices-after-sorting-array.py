class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less_than_target = 0
        for i in nums:
            if i < target:
                less_than_target += 1

        repeated = nums.count(target)
        result = []
        for i in range(less_than_target,less_than_target + repeated):
            result.append(i)
            
        return result