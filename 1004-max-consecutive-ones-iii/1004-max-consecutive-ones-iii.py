class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = right = 0
        for right in range(len(A)):
            if A[right] == 0:
                K -= 1
            if K < 0:
                if A[left] == 0:
                    K += 1
                left += 1
        return right - left + 1