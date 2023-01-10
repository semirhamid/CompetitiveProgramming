class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mn = sys.maxsize
        left = 0
        count = {}
        for right in range(len(cards)):
            if count.get(cards[right], False):
                count[cards[right]] += 1
                while count[cards[right]] != 1:
                    count[cards[left]] -= 1
                    left += 1
                mn = min(mn, right - left + 2)
            else:
                count[cards[right]] = 1 + count.get(cards[right], 0)
        return mn if mn != sys.maxsize else -1