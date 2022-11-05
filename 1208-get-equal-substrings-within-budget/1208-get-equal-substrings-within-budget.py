class Solution:
    def equalSubstring(self, s, t, cost):
        i = 0
        for j in range(len(s)):
            cost -= abs(ord(s[j]) - ord(t[j]))
            if cost < 0:
                cost += abs(ord(s[i]) - ord(t[i]))
                i += 1
        return j - i + 1