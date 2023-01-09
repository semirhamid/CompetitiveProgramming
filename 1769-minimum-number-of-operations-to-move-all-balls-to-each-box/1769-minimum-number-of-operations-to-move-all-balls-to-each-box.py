class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxs = { i:boxes[i] for i in range(len(boxes)) if boxes[i] == "1"}
        result = []
        for i in range(len(boxes)):
            sm = 0
            for j in boxs:
                if j != i:
                    sm += abs(i - j) 
            result.append(sm)
        return result