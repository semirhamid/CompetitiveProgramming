class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified = ""
        for char in s:
            if char.isalnum():
                modified += char.lower()
        reversed = modified[::-1]
        return modified == reversed