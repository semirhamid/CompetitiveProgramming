class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        d = [1] + [0] * K # range of key is 0 <= key < K because key always mod by K
        acc = 0
        for a in A:
            acc = (acc + a) % K # it's works because a % k % k % k .... n times is still same as a % k 
            if d[acc]:
                res += d[acc]
            d[acc] += 1            
        return res