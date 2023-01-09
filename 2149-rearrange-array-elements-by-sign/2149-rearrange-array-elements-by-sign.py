class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative = [i for i in nums if i < 0]
        positive = [i for i in nums if i > 0]
        result = []
        left = 0
        right = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(positive[left])
                left += 1
            else:
                result.append(negative[right])
                right += 1
        return result
            