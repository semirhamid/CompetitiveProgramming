class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix = 0
        for i in range(len(chalk)):
            prefix += chalk[i]
            chalk[i] = prefix
        k = k % chalk[-1]
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
        return -1