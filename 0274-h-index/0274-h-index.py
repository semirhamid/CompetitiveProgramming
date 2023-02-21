class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        right = 0
        for i in range(len(citations)):
            if citations[i]<=right:
                break
            right +=1
        return right