class Solution:
    def printVertically(self, s: str) -> List[str]:
        splitted = s.split()
        length = len(splitted)
        result = []
        mx = 0
        for i in splitted:
            mx = max(mx, len(i))
        for k in range(len(splitted)):
            splitted[k] = splitted[k] + (mx - len(splitted[k]) ) * " "
            
        for i in range(len(splitted[0])):
            word = ""
            for j in range(len(splitted)):
                word+= splitted[j][i]
            result.append(word.rstrip())
        return result
            