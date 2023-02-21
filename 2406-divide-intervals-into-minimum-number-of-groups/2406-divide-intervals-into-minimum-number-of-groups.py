class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        A = []
        for a,b in intervals:
            A.append([a, 1])
            A.append([b + 1, -1])
        res = cur = 0
        for a, diff in sorted(A):
            cur += diff
            res = max(res, cur)
        return res