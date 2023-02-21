class Solution(object):
    def findMaxLength(self, nums):
        count = 0
        max_length=0
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            count += -1 if num == 0 else 1
            
            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index
        
        return max_length