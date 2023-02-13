class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        per = permutations(nums)
        l = []
        for i in per:
            if i not in l:
                l.append(i)
        return l      