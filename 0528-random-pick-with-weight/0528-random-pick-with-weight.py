import bisect
import random

class Solution:

    def __init__(self, w: List[int]):

        w=list(map(lambda x:x/sum(w),w))
        for x in range(1,len(w)) :
            w[x]+=w[x-1]
        self.w=w
        
    
        

    def pickIndex(self) -> int:
        r=random.uniform(0,1)
        return bisect.bisect_left(self.w,r)