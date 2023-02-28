class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        arr = [1] 
        prev =  self.getRow(rowIndex - 1)
        for i in range(1, len(prev)):
            arr.append(prev[i] + prev[i - 1])
        arr.append(1)
        return arr