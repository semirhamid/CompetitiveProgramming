class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        converted = Counter(changed)
        if converted[0] % 2:
            return []

        for x in sorted(converted):
            if converted[x] > converted[2 * x]:
                return []
            else:
                if x == 0:
                    converted[2 * x] = converted[x] // 2
                else:
                    converted[2 * x] -= converted[x]

        return list(converted.elements())