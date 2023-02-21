class Solution:
    def longestNiceSubarray(self, A):
        res = AND = i = 0
        for j in range(len(A)):
            while AND & A[j]:
                AND ^= A[i]
                i += 1
            AND |= A[j]
            res = max(res, j - i + 1)
        return res