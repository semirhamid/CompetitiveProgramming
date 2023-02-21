class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0: return True
        for i in range(math.ceil(math.sqrt(c))):
            other = math.sqrt(c - (i * i))
            if other >= 0 and other.is_integer() and int(other) == int(math.ceil(other)):
                return True
        return False