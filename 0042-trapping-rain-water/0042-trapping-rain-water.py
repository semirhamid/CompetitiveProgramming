class Solution:
    def trap(self, tank: List[int]) -> int:
        maxLeft = tank[0]
        maxRight = tank[-1]
        left = 0
        right = len(tank) - 1
        water = 0
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, tank[left])
                water += maxLeft - tank[left]
            else:
                right -= 1
                maxRight = max(maxRight, tank[right])
                water += maxRight - tank[right]
        return water