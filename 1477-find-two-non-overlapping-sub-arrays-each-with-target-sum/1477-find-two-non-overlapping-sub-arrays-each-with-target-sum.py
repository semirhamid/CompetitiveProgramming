class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = {0: -1}
        best_till = [math.inf] * len(arr)
        ans = best = math.inf
        for i, curr in enumerate(itertools.accumulate(arr)):
            if curr - target in prefix:
                end = prefix[curr - target]
                if end > -1:
                    ans = min(ans, i - end + best_till[end])
                best = min(best, i - end)
            best_till[i] = best
            prefix[curr] = i
        return -1 if ans == math.inf else ans