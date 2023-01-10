class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = {}
        for left in range(len(s) - 9):
            right = left + 10
            if dic.get(s[left:right], False):
                dic[s[left:right]] += 1
            else:
                dic[s[left:right]] = 1

        result = []
        for i in dic:
            if dic[i]> 1:
                result.append(i)
        return result