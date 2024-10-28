class Solution:
    def simplifyPath(self, path: str) -> str:
        path, stack = [p for p in path.split("/") if p], []
        for p in path:
            if p == "..": 
                if stack: 
                    stack.pop()
            elif p != ".": stack.append(p)
        return "/" + "/".join(stack)
        