class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        unique = Counter(nums)
        lst = list(unique.keys())
        lst.sort()
        left = 0
        response = {}
        right = len(lst) - 1
        while left <= right:
            if unique[lst[left]] == 0:
                left += 1
            elif unique[lst[right]] == 0:
                right -= 1
            else:
                response[(lst[right] + lst[left])/2] = 0
                unique[lst[right]] -= 1
                unique[lst[left]] -= 1

        return len(response)