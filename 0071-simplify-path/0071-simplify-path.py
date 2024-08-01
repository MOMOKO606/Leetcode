class Solution:
    def simplifyPath(self, path: str) -> str:
        path, stack = [folder for folder in path.split("/") if folder], []
        for folder in path:
            if folder == ".": continue
            if folder == "..": 
                if stack: stack.pop()
            else:
                stack.append(folder)
        return "/" + "/".join(stack)
        