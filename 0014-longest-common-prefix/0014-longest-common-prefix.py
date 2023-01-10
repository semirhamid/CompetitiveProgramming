class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mn = 201
        left = 0
        for i in range(len(strs)):
            mn = min(mn, len(strs[i]))
        for i in range(mn):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]
            left = i + 1
        return strs[0][:left]