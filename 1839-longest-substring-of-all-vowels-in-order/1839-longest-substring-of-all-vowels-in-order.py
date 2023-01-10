class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ans = ii = 0
        unique = 1
        for i in range(1, len(word)): 
            if word[i-1] > word[i]: 
                ii = i 
                unique = 1
            elif word[i-1] < word[i]: unique += 1
            if unique == 5: ans = max(ans, i-ii+1)
        return ans 