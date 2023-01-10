class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        length = len(arr)
        result = []
        for i in range(length,0,-1):
            max_idx = arr.index(i)
            if i==0 or i==1:
                continue
            if max_idx == length -1:
                continue
            x = arr[max_idx::-1]
            arr[:max_idx+1] = x
            result.append(len(x))
            y = self.flip(arr[:i])
            arr[:i] = y
            result.append(len(y))
            print(arr)
        return result


    def flip(self,arr):
        return arr[-1::-1]