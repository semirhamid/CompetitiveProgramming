class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.extend([float('-inf'), float('inf')])
        heaters.sort()
        houses.sort()
        rad = 0
        i  = 1
        for house in houses:
            while heaters[i] < house:
                i += 1
            min_dist = min(house - heaters[i - 1] , heaters[i] - house)
            rad = max(rad , min_dist)
        return rad