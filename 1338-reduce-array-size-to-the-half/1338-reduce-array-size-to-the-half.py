class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = dict()
        for i in arr:
            if i in count:
                count[i]+=1
            else:
                count[i] = 1
        new = sorted(count,key=lambda x:count[x], reverse=True)
        size = len(arr)
        counter = 0
        elements = 0
        for i in new:
            counter += count[i]
            elements +=1
            if counter >= (size//2):
                break
        return elements