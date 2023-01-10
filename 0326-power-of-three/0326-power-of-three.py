class Solution:
    def isPowerOfThree(self, n, count=0) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return n % 3 == 0 and self.isPowerOfThree(n/3)