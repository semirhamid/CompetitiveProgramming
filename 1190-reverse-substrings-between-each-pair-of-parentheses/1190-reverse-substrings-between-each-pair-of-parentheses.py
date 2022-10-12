class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ")":
                stack.append(i)
            else:
                new = []
                while stack[-1] != "(":
                    new.append(stack.pop())
                stack.pop()
                for i in range(len(new)):
                    stack.append(new[i])
        return "".join(stack)