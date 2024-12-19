class Solution:
    def smallestSubsequence(self, s: str) -> str:
        indexes, visited, stack = {char: i for i, char in enumerate(s)}, set(), []
        for i, char in enumerate(s):
            if char in visited: continue
            while stack and char < stack[-1] and indexes[stack[-1]] > i:   
                visited.remove(stack.pop())
            stack.append(char)
            visited.add(char)
        return "".join(stack)
        