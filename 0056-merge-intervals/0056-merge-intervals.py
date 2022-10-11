class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        overlap = []
        if(n<=1):
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        for interval in intervals:
            if len(overlap) == 0 or interval[0] > overlap[-1][1]:
                overlap.append(interval)
            else:
                overlap[-1][1] = max(interval[1], overlap[-1][1])

        return overlap