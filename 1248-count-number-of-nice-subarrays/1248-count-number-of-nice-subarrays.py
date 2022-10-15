class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        memo = collections.Counter()
        memo[0] = 1
        res = odds = 0
        for x in nums:
            if x % 2:
                odds += 1
            memo[odds] += 1
            res += memo[odds-k]
        return res