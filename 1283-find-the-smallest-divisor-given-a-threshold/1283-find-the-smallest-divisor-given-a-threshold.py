class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def checkDivision(num):
            sm = 0
            for i in nums:
                sm += math.ceil(i / num)
            return sm
        low = 1
        high =  max(nums)
        while low < high:
            mid = (low + high) // 2
            res = checkDivision(mid)
            if res > threshold:
                low = mid + 1
            else:
                high = mid 
        return low