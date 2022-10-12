class Solution:
    def isValid(self, s: str) -> bool:
        bucket = []
        pairs = {"{": "}", "[": "]", "(":")"}
        for i in s:
            if i == "{" or i== "(" or i=="[":
                bucket.append(i)
            else:
                if len(bucket)==0:
                    return False
                if pairs[bucket.pop()] == i:
                    continue
                else:
                    return False
        if len(bucket) >0:
            return False
        return True