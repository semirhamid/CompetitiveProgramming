class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            result.append(self.arthimetic_checker(nums[l[i]:r[i]+1]))
        return result
    
    def arthimetic_checker(self,num):
        unique = set(num)
        ma = max(num)
        mn = min(num)
        if len(num) != len(unique): return len(unique) == 1  # take care of duplicates
        if (ma - mn) % (len(num) - 1) != 0: return False
        diff = (ma - mn) // (len(num) - 1)
        for i in range(mn, ma , diff):
            if i not in unique:
                return False
        return True
        