class Solution:
    def canMakePaliQueries(self, s, queries):
        dp = [[0] * 26]
        for i in range(1, len(s)+1):
            new = dp[i-1][:]
            j = ord(s[i-1]) - 97
            new[j] += 1
            dp.append(new)
        ans = []
        for l, r, k in queries:
            L = dp[l]
            R = dp[r+1]
            ans.append(sum((R[i] - L[i]) & 1 for i in range(26)) // 2 <= k)
        return ans
        