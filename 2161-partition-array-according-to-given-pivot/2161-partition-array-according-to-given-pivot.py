class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        middle = []
        after = []
        for i in nums:
            if i  < pivot:
                before.append(i)
            elif i == pivot:
                middle.append(i)
            else:
                after.append(i)
        return before + middle + after