class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = [0] * (len(words) + 2)
        st = {"a","e","o","i","u"}
        result = []
        for i in range(len(words)):
            if words[i][0] in st and  words[i][-1] in st:
                ans[i + 1] += 1
        for i in range(1, len(ans)):
            ans[i] += ans[i - 1]
        for query in queries:
            result.append(ans[query[1] + 1] - ans[query[0]])
        return result