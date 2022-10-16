class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        holder = [0 for i in range(1000)]
        for trip in trips:
            if trip[0]>capacity: return False
            for j in range(trip[1], trip[2]):
                if holder[j] + trip[0] > capacity:
                    return False
                else:
                    holder[j] += trip[0]
        return True