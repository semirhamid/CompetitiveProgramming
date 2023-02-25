class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        a,n=[],len(s)
        c=t=0
        for i in range(1,n):
            if s[i]=='(':
                t+=1
            elif s[i-1]=='(':
                c+=1<<t
                t-=1
            else:
                t-=1
        return c