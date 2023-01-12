class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word = [i for i in words[0]]
        word = Counter(word) 
        result = []
        for j in word:
            mn = word[j]
            flag = True
            for wor in words:
                if j not in wor:
                    flag = False
                    break
                wor = Counter(wor)
                mn = min(wor[j], mn)
                    
            if flag :
                for i in range(mn):
                    result.append(j)
        return result