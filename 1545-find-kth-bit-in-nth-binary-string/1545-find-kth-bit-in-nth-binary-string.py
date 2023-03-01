class Solution:
    def __init__(self):
        self.memo = {}
        self.inverted = {}
    def findKthBit(self, n: int, k: int) -> str:
        return self.find(n)[k - 1]
    
    def find(self, n):
        
        if n == 1:
            return "0"
        if n not in self.memo:
            self.memo[n] = self.find(n - 1) + "1" + self.invert(n - 1)[::-1]
        return self.memo[n]


    def invert(self, n):
        if n == 1:
            return "1"
        if n not in self.inverted:
            text = self.find(n)
            new = ""
            for i in range(len(text)):
                new += "0" if text[i] == "1" else "1"
            self.inverted[n] = new
        
        return self.inverted[n]
        