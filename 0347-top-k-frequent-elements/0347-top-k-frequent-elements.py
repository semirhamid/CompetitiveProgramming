class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        empty = dict()
        for i in nums:
            if i in empty:
                empty[i]+=1
            else:
                empty[i]=1
        st = sorted(empty,key=lambda x:empty[x], reverse=True)
        return st[:k]
        
                    