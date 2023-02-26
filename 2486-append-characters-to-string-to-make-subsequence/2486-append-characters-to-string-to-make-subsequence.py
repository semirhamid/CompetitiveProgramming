class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx, n = 0, len(t)
        for c in s:
            if idx < n and t[idx] == c:
                idx += 1
        return n - idx