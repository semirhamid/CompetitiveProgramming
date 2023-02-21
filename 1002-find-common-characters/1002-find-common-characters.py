class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word = [i for i in words[0]]
        container = []
        for current_word in words:
            letter_count = [0 for i in range(26)]
            for char in current_word:
                letter_count[ord(char) - 97] += 1
            container.append(letter_count)
            
        result = []
        for i in range(26):
            mn =  container[0][i]
            for wor in container:
                mn = min(mn, wor[i])
            for j in range(mn):
                    result.append(chr(97 + i))
                         
        return result