class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repeated = dict()
        for i in nums:
            if i in repeated:
                repeated[i]+=1
            else:
                repeated[i]=1
        st = sorted(repeated,key=lambda x:repeated[x], reverse=True)
        return st[:k]
        
                    
