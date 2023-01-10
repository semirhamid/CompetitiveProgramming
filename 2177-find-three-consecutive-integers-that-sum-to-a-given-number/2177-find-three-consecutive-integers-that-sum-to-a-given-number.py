class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        temp = num - 3
        return self.findSum(temp // 3, num)
    def findSum(self, start, target):
        arr = [i for i in range(start , start + 6)]
        for i in range(len(arr) - 3):
            if sum(arr[i:i + 3]) == target:
                return arr[i:i + 3]
        return []
        