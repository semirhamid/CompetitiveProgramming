class Solution:
    def isPowerOfFour(self, n, count=0) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 4 != 0:
            return False
        return n % 4 == 0 and self.isPowerOfFour(n/4)