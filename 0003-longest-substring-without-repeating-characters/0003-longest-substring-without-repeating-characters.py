class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left= 0
        right=1
        if len(s)==0:
            return 0
        maxVal = set(s[0])
        length = 1
        while right < len(s):
            if s[right ] in maxVal:
                maxVal.remove(s[left])
                left += 1
            else:
                maxVal.add(s[right])
                right +=1
                length = max(length,len(maxVal))
        return  length