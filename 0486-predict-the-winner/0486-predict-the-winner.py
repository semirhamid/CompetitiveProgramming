class Solution:
    def PredictTheWinner(self, nums):
        dp = {}
        def getscore(left, right, turn):
            if left == right:
                return nums[left]
            if (left + 1, right) not in dp:
                dp[(left + 1, right)] = getscore(left + 1, right , not turn)            
            getLeft =  nums[left] + dp[(left + 1, right)]
            if (left , right - 1) not in dp:
                dp[(left , right - 1)] = getscore(left , right - 1 , not turn)
            getRight =  nums[right] + dp[(left, right - 1)]
            
            if turn:
                return max(getLeft, getRight)
            else:
                return min(getscore(left + 1, right , not turn), getscore(left, right - 1, not turn))
        result = getscore(0, len(nums) - 1, nums)
        return result >= sum(nums) - result
