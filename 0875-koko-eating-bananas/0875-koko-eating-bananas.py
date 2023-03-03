class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkPartition(limit):
            hour = 0
            cur = 0
            for val in piles:
                if val < limit or val == limit:
                    hour += 1
                else:
                    hour += val // limit
                    mod = val % limit 
                    hour += 1 if mod > 0 else 0

            # count the last hour
            if cur > 0:
                hour += 1
            return hour
        hours = h
        low = 1
        high = max(piles)
        if hours == 1:
            return high
        while low < high:
            mid = (high + low) // 2
            hour = checkPartition(mid)
            if hour <= hours:
                high = mid
            else:
                low = mid + 1

        return low