class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        left = 0
        result = [] 
        while left < len(source):
            double = source[left].find("//")
            star = source[left].find("/*")
            if double == -1:
                double = 101
            if star == -1:
                star = 101
            if double < star :
                word = source[left][:double]
                if len(word) != 0:
                    result.append(word)
                left += 1
            elif star < double:
                gra = source[left][:star]
                closing = source[left][star + 2:].find("*/")
                if closing == -1:
                    while closing == -1:
                        left += 1
                        closing = source[left].find("*/")
                else:
                    closing += 2 + star
                next_line = gra  + source[left][closing + 2:]
                source[left] = next_line

            else:
                if source[left] != "":
                    result.append(source[left])
                left += 1
        return result
                
                
            