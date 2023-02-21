class Solution:
    def __init__(self):
        self.memo = {}
    def fib(self, N: int) -> int:
        if N == 0: return 0
        if N == 1: return 1
        if N-1 not in self.memo: self.memo[N-1] = self.fib(N-1)
        if N-2 not in self.memo: self.memo[N-2] = self.fib(N-2)

        return self.memo[N-1] + self.memo[N-2]