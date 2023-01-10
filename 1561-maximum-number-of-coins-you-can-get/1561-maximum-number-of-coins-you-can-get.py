class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        size = len(piles)//3
        count = 0
        if size == 0:
            return 0
        for i in range(size):
            count += piles[(len(piles)-2)-2*i]
        return count
