class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            mn = i
            for j in range(i , len(names)):
                if heights[j] > heights[mn]:
                    mn = j
            names[i] , names[mn] = names[mn] , names[i]
            heights[i] , heights[mn] = heights[mn] , heights[i]
        return names
                
                