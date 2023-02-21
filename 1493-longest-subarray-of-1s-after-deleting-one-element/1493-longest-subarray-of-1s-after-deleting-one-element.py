class Solution:
    def longestSubarray(self, A: List[int]) -> int:
        max_zero = 0
        left = 0
        mx = 0
        for right in range(len(A)):
            if A[right] == 0:
                max_zero += 1

            while max_zero > 1:
                if  left < len(A) and  A[left]==0:
                    max_zero -= 1
                if max_zero > 0 :
                    left += 1
            if max_zero == 0:
                temp = right - left
            else:
                temp = (right - left) +1 -max_zero
            mx = max(mx, temp)
        return mx