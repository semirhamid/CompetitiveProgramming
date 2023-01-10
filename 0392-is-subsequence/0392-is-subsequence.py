class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first = 0
        if not s : return True
        for i in t:
            if s[first] == i: first += 1
            if first == len(s): return True
        return False