class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        length = len(nums)
        prefix = [0] + [0] * length
        cur = 0
        for i , j in requests:
            prefix[j + 1] -= 1
            prefix[i] += 1
        for i in range(length + 1):
            cur += prefix[i]
            prefix[i] = cur
        new_prefix = sorted(prefix, reverse = True)
        new_nums = sorted(nums, reverse = True)
        count = 0
        for right in range(length):
            count += new_nums[right] * new_prefix[right]
        return count % (10**9 + 7)
 














    
#                 mx = 0
#         for i in range(length ):
#             cur += nums[i]
#             prefix[i + 1] = cur
#         print(prefix)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    