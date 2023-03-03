# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            if isBadVersion(high) and not isBadVersion(high - 1):
                return high
            elif isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(low) and not isBadVersion(low - 1):
                return low
            if not isBadVersion(mid):
                low = mid + 1
            else:
                high = mid - 1
        return mid
                
        