class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        left = 0
        count = 0
        for i in s:
            if g[left] <= i:
                count += 1
                left += 1
            if left == len(g):
                break
        return count