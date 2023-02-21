class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mn = 100000
        idx = -1
        for i in range(len(points)):
            if points[i][0] != x and points[i][1] != y:
                pass
            else:
                x1 = points[i][0]
                y1 = points[i][1]
                temp_dist = abs(x1 - x) + abs(y1 - y)
                if temp_dist < mn:
                    mn = temp_dist
                    idx = i
        return idx