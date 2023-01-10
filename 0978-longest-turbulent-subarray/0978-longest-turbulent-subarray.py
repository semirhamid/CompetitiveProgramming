class Solution:
    def maxTurbulenceSize(self, A):
        best = clen = 0

        for i in range(len(A)):
            if i >= 2 and (A[i-2] > A[i-1] < A[i] or A[i-2] < A[i-1] > A[i]):
                clen += 1
            elif i >= 1 and A[i-1] != A[i]:
                clen = 2
            else:
                clen = 1
            best = max(best, clen)
        return best
        