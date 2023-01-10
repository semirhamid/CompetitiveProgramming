class Solution:
    def dailyTemperatures(self, T):
        ans, n = [0]*len(T), len(T)
        for cur in range(n-2,-1,-1):
            nxt = cur+1
            while nxt < n and T[nxt] <= T[cur]:
                nxt += ans[nxt] if ans[nxt] else n
            ans[cur] = nxt-cur if nxt < n else 0
        return ans