class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for right in range(len(s) - 2):
            if len(set(s[right: right + 3])) == 3: count += 1
        return count