class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word = [i for i in words[0]]
        container = []
        for current_word in words:
            letter_count = [0 for i in range(26)]
            offset = ord('a')
            for char in current_word:
                letter_count[ord(char) - offset] += 1
            
            container.append(letter_count)
        result = []
        current = container[0]
        for i in range(26):
            flag = True
            mn =  container[0][i]
            for wor in container:
                if  wor[i] == 0:
                    flag = False
                mn = min(mn, wor[i])
            if flag:
                for j in range(mn):
                    result.append(chr(ord('a') + i))
                         
        return result