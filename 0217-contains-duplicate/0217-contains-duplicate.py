class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for item in count.keys():
            if count[item] > 1:
                return True
        return False