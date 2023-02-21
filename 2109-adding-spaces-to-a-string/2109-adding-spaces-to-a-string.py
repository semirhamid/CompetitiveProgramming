class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        for right in range(len(spaces)):
            if right == 0:
                result += s[:spaces[right]]
                result += " "
            else:
                result += s[spaces[right - 1]:spaces[right]]
                result += " "
        result += s[spaces[-1]:]
        return "".join(result)
                
            
            