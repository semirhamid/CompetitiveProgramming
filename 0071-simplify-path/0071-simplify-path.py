class Solution:
    def simplifyPath(self, path: str) -> str:
        levels, stack = path.split("/"), []

        for l in levels:
            if len(l)>0 and l != '.':
                if l == '..' and stack:
                    stack.pop()
                elif l != '..':
                    stack.append(l)
        
        return "/"+"/".join(stack)