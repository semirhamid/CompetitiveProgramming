class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = dict(Counter(blocks[:k]))
        mn = count.get("W", 0)
        left = 0
        for right in range(k, len(blocks)):
            count[blocks[right]] = 1 + count.get(blocks[right], 0)
            count[blocks[left]] -= 1
            left += 1
            mn = min(mn, count.get("W", 101))
        return mn