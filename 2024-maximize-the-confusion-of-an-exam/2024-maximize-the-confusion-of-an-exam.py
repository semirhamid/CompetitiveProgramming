class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        letters = {}
        left = count = sm = 0
        for right in range(len(answerKey)):
            letters[answerKey[right]] = 1 + letters.get(answerKey[right], 0)
            sm += 1
            while len(letters) == 2 and min(letters.values()) > k:
                letters[answerKey[left]] -= 1
                left += 1
                sm -= 1
            count = max(count, sm)

        return count
