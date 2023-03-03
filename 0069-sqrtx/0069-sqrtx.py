class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:  # 3 4
            mid = low + (high - low) // 2  # 2
            temp = mid * mid  # 4
            temp_lower = (mid - 1) * (mid - 1)
            temp_higher = (mid + 1) * (mid + 1)
            if temp == x:
                return mid
            elif temp_lower < x and temp_higher > x:
                if temp > x:
                    return mid - 1
                elif temp < x:
                    return mid

            elif temp > x:  # True
                high = mid
            else:
                low = mid + 1
        return mid