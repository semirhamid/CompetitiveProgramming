class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum() and s[left].lower() != s[right].lower():
                return False
            elif not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                left += 1
                right -= 1

        return True
