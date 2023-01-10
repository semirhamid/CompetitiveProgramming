class Solution:
    def minimumBuckets(self, s):
        return -1 if search('(^|H)H(H|$)', s) else s.count('H') - s.count('H.H')
            