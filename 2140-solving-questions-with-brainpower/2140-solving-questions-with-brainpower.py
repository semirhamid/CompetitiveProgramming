class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        result = [0] * length
        for i in range(length - 1, -1, -1):
            next_idx = questions[i][1] + i + 1
            if next_idx < length:
                result[i] = questions[i][0] + result[next_idx]
            else:
                result[i] = questions[i][0]

            if i < length - 1:
                result[i] = max(result[i], result[i + 1])
        return result[0]