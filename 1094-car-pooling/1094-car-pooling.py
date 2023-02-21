class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        holder = [0] * 1001
        for trip in trips:
            holder[trip[1]] += trip[0]
            holder[trip[2]] -= trip[0]
        prefix = 0
        for i in holder:
            prefix += i
            if prefix > capacity:
                return False
        return True