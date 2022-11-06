class Solution:
    def answerQueries(self, A: List[int], queries: List[int]) -> List[int]:
        A = list(accumulate(sorted(A)))
        return [bisect_right(A, q) for q in queries]
        