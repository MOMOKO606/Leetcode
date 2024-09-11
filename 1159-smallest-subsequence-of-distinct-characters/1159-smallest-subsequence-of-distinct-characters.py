class Solution:
    def smallestSubsequence(self, s: str) -> str:
        visited, boundaries, stack = set(), {char: i for i, char in enumerate(s)}, []
        for i, char in enumerate(s):
            if char in visited: continue
            while stack and char < stack[-1] and boundaries[stack[-1]] > i:
                visited.remove(stack.pop())
            visited.add(char)
            stack.append(char)
        return "".join(stack)
        