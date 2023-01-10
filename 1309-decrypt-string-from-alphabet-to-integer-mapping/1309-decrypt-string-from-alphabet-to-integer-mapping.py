class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic = {}
        a = 97
        for i in range(1,27):
            if i < 10:
                dic[str(i)] = chr(a)
            else :
                dic[str(i) + "#"] = chr(a)
            a += 1
        left = 0
        result = ""
        while left + 2 < len(s) :
            if s[left + 2] == "#":
                key = s[left:left + 3]
                result += dic[key]
                left += 3
            else:
                key = s[left]
                result += dic[key]
                left += 1
        while left < len(s) :
            result += dic[s[left]]
            left += 1

        return result