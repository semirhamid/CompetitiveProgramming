class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        new = []
        value = {}
        for i in range(n):
            value[i]= points[i][0] **2 + points[i][1] **2
        value = {k: v for k, v in sorted(value.items(), key=lambda item: item[1])}

        for i in value:
            new.append(points[i])
        return new[:k]