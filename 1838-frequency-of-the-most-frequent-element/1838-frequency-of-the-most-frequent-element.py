class Solution:
    def maxFrequency(self, A: List[int], k: int) -> int:
        i = 0
        A.sort()
        for j in range(len(A)):
            k += A[j]
            if k < A[j] * (j - i + 1):
                k -= A[i]
                i += 1
        return j - i + 1