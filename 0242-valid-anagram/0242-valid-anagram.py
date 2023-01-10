class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = Counter(t)
        count2 = Counter(s)
        for item in count1.keys():
            if count1[item] != count2[item]:
                return False
        return True if len(t) == len(s) else False