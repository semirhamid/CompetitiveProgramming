class Solution:
    def average(self, salary: List[int]) -> float:
        mn = mx = salary[0]
        sm = 0
        for i in salary:
            sm += i
            mn = min(mn, i)
            mx = max(mx, i)
        return (sm - mn - mx) / (len(salary) - 2)
        