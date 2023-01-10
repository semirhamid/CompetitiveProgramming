class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        res = [-1] * length
        if length < (2 * k + 1): return res
        sm = sum(nums[: (k + k + 1)])
        res[k] = sm // (2 * k + 1)
        for i in range(k + 1, length - k ):
            sm += nums[i + k]
            sm -= nums[i - k - 1]
            res[i] = sm // (2 * k + 1)
        return res