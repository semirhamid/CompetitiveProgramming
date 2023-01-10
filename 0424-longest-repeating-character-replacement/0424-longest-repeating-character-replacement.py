class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_f = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            max_f = max(max_f, sum(count.values()))

        return max_f