class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot = (n**2 + n) / 2
        if pivot % math.sqrt(pivot) == 0:
            return int(math.sqrt(pivot))
        
        return -1