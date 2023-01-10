class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = 0
        result = []
        for i in range(len(arr)):
            prefix ^= arr[i]
            arr[i] = prefix
        for query in queries:
            left = arr[query[0] - 1] if query[0] != 0 else 0
            result.append(left ^ arr[query[1]])
        return result