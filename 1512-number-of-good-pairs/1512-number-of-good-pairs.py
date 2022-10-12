class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_pairs = Counter(nums)
        sum = 0
        for i in num_pairs.values():
            sum += (i * (i-1))//2
        return sum