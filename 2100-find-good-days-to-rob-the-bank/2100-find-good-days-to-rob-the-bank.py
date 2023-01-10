class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        length = len(security)
        prefix = [0] * length
        for i in range(1, length):
            if security[i] <= security[i - 1]:
                prefix[i] = prefix[i - 1] + 1
        postfix = [0] * length
        for i in range(length -2, -1, -1):
            if security[i] <= security[i + 1]:
                postfix[i] = postfix[i + 1] + 1
        result = []
        for i in range(length):
            if prefix[i] >= time and postfix[i] >= time:
                result.append(i)
        return result