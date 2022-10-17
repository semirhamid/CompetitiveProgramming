class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay_len = len(haystack)
        stack = []
        for i in range(hay_len):
            if haystack[i] == needle[0]:
                stack.append(i)
        nee_len = len(needle)
        for i in stack:
            count = 0
            left = 0
            while i < hay_len:
                if haystack[i] == needle[left]:
                    left += 1
                    i += 1
                    count += 1
                else: break
                if count == nee_len:return i - count
        return -1