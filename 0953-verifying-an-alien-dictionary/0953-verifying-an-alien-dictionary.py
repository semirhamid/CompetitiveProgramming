class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabets = {}
        for i in range(len(order)):
            alphabets[order[i]] = i
        for i in range(len(words) - 1):
            left = 0
            right = 0
            flag = True
            while left < len(words[i]) and right < len(words[i + 1]):
                if alphabets[words[i][left]] < alphabets[words[i + 1][right]]:
                    flag = True
                    break
                elif alphabets[words[i][left]] == alphabets[words[i + 1][right]]:
                    flag = False
                    right += 1
                    left += 1
                else:
                    return False
            if not flag:
                if len(words[i]) > len(words[i + 1]):
                    return False

        return True