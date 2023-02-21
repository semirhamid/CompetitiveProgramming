class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        # If length of string is less than 2, there is no way we can get a nice substring out of it
        if len(s) < 2 : return ""
        
        # A set of all characters in the given string
        ulSet = set(s)
        
        for i,c in enumerate(s):
            # If character is lowercase and the set does not have its uppercase variation or vice versa
            # It means that we need to not consider this character at all and so, find the longest substring till this character and after this character
            # Repeat this till we reach the end
            if c.swapcase() not in ulSet:
                s1 = self.longestNiceSubstring(s[0:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                
                return s2 if len(s2) > len(s1) else s1
        
        
        # If the above recursive calls don't happen that means our string has each character in lowercase and uppercase already so we can return it
        return s