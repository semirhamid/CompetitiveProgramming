class Solution:
    def reverseVowels(self, s: str) -> str:
        dic = "aeiouAEIOU"
        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            while s[left] not in dic and left < right:
                left += 1
            while s[right] not in dic and right > left:
                right -= 1
            s[left] , s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)