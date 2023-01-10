class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefixs = {0:1}

        for i in nums:
            current_sum += i
            diff = current_sum - k
            count += prefixs.get(diff, 0)
            prefixs[current_sum] = 1 + prefixs.get(current_sum, 0)
        return count