class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(1, len(names)):
            k  = i
            while k > 0 and  heights[k] > heights[k - 1]:
                names[k] , names[k - 1] = names[k - 1] , names[k]
                heights[k] , heights[k - 1] = heights[k - 1] , heights[k]
                k -= 1
                    
        return names
                