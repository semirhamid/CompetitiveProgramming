class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0) + 1
        for i in t:
            if i in dic:
                if dic[i] == 0:
                    return i
                else:
                    dic[i] -= 1
            else:
                return i
