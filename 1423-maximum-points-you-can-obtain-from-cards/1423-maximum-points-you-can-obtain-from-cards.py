class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        tot = sum(cardPoints)
        length = len(cardPoints)
        left = 0
        right = length - k
        mn = sum(cardPoints[:right])
        temp = mn
        while right < length :
            temp += cardPoints[right]
            temp -= cardPoints[left]
            mn = min(temp, mn)
            right += 1
            left += 1

        return tot - mn 