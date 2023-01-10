class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = {"0": 0, "1": 0, "01": 0, "10": 0}
        count = 0
        for i in range(len(s)):
            if s[i] == "0":
                dp["0"] += 1
                dp["10"] += dp["1"]
                count += dp["01"]
            else:
                dp["1"] += 1
                dp["01"] += dp["0"]
                count += dp["10"]

        return count