class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cur = 0
        remainders = {0:-1}
        for idx, val in enumerate(nums):
            cur += val
            rem = cur % k
            if rem not in remainders:
                remainders[rem] = idx
            elif idx - remainders[rem] > 1:
                return True
        return False
