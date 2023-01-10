class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for com in cpdomains:
            num = int(com.split(" ")[0])
            for i in range(1, len(com) + 1):
                if com[-i] == "." or com[-i] ==" ":
                    dic[com[-i + 1:]] = dic.get(com[-i + 1:], 0) + num
        temp = []
        for i in dic:
            temp.append(str(dic[i]) + " " + i)

        return temp