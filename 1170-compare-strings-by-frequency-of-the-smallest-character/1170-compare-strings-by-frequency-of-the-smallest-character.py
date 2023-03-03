class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        query = [q.count(min(q)) for q in queries]
        word = [w.count(min(w)) for w in words]
        word.sort()
        ans = []
        for cnt in query:
            ans.append(len(word) - bisect_right(word, cnt))

        return ans