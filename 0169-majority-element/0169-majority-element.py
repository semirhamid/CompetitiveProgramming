class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums) / 2
        for item in count.keys():
            if count[item] > n:
                return item
        return count