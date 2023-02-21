class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted([int(i) for i in nums])
        return str(nums[-k])