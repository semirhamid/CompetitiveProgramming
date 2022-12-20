class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        left = 0
        right = 0
        current = 0
        while left < len(word1) and right < len(word2):
            if current % 2 == 0:
                result += word1[left]
                left += 1
            else:
                result += word2[right]
                right += 1
            current += 1
        while right  < len(word2):
            result += word2[right ]
            right += 1
        while left  < len(word1):
            result += word1[left ]
            left += 1
        return result