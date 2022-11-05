class Solution:
    def maxRepOpt1(self, S: str) -> int:
        A = [[c, len(list(g))] for c, g in itertools.groupby(S)]
        # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
        count = collections.Counter(S)
        # only extend 1 more, use min here to avoid the case that there's no extra char to extend
        res = max(min(k + 1, count[c]) for c, k in A)
        # merge 2 groups together
        for i in range(1, len(A) - 1):
            # if both sides have the same char and are separated by only 1 char
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                # min here serves the same purpose
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res