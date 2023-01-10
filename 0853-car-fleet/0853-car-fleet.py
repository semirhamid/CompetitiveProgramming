class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [ (target - position[i])/speed[i] for i in range(len(position))]
        res = list(zip(position,pair))
        bucket = []
        pair = sorted(res,key= lambda res : res[0], reverse=True)
        for i in pair:
            if len(bucket) !=0 and i[1]<=bucket[-1][1]:
                pass
            else:
                bucket.append(i)
        return len(bucket)