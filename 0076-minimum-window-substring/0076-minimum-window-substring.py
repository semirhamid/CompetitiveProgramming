class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dic = Counter(t)
        s_dic = {}
        left = 0
        result = ""
        for right in range(len(s)):
            s_dic[s[right]] = s_dic.get(s[right], 0) + 1
            while self.dicCheck(s_dic, t_dic):
                if len(result) > right - left + 1 or result == "":
                    result = s[left: right + 1]
                s_dic[s[left]] -= 1
                if s_dic[s[left]] == 0:
                    s_dic.pop(s[left])
                left += 1
        return result 
    
    def dicCheck(self, s_dic, t_dic):
        for i in t_dic.keys():
            if i not in s_dic:
                return False
            if t_dic[i] > s_dic[i]:
                return False
        return True
                