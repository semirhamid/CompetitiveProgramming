class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        stack = []
        left = 0
        right = 0
        prev  = 0

        while right < len(s):
            while left < right+1:
                if s[left] in s[right+1:]:
                    right += 1
                else:
                    left +=1
            stack.append((right-prev)+1)
            prev = right +1
            right+=1
            left = right
        return stack