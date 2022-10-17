class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        length = len(s)
        left = length - 1
        right = length - 1
        while left > -1 :
            if s[left] == " ":
                result.append(s[left + 1:right + 1])
                while left > 0 and s[left] == " ":
                    left -= 1
                right = left

            left -= 1
        result.append(s[0:right + 1])

        return " ".join(result).strip()