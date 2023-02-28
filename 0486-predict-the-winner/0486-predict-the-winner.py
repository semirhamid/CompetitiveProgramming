class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def getscore(left, right, turn):
            if left == right:
                return nums[left] * turn
            
            getleft = nums[left]*turn + getscore(left+1, right, -turn)
            getright = nums[right]*turn + getscore(left, right-1, -turn)
            
            if turn == 1:
                return max(getleft, getright)
            elif turn == -1:
                return min(getleft, getright)
            
        if getscore(0, len(nums)-1, 1) >= 0:
            return True
        else:
            return False