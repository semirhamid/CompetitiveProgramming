class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while right > left:
            sm = numbers[right] + numbers[left]
            if sm  == target:
                return [left + 1, right + 1]
            if sm < target:
                while numbers[left] == numbers[left + 1]:
                    left += 1
                left += 1
            else:
                while numbers[right] == numbers[right - 1]:
                    right -= 1
                right -= 1
        
            