class Solution:
    def Solve(self, candidates, target, sum, output, ans, index):
        if target == sum:
            output.append(list(ans))
            return
        if len(candidates) == index:
            return
        if sum > target:
            return
        ans.append(candidates[index])
        self.Solve(candidates, target, sum + candidates[index], output, ans, index + 1)
        ans.pop()
        while index < len(candidates)-1 and candidates[index] == candidates[index + 1]:
            index += 1
        self.Solve(candidates, target, sum, output, ans, index + 1)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        ans = []
        candidates.sort()
        self.Solve(candidates, target, 0, output, ans, 0)
        return output