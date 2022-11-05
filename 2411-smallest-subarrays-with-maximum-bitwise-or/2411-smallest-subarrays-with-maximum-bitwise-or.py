class Solution:
    def smallestSubarrays(self, A):
        last = [0] * 32
        n = len(A)
        res = [0] * n
        for i in range(n - 1, -1, -1):
            for j in range(32):
                if A[i] & (1 << j):
                    last[j] = i
            res[i] = max(1, max(last) - i + 1)
        return res