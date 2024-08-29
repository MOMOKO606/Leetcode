class Solution:
    def smallestSubsequence(self, s: str) -> str:
        boundaries, stack, visited = {char: i for i, char in enumerate(s)}, [], set()
        for i, char in enumerate(s):
            if char in visited: continue
            while stack and stack[-1] > char and boundaries[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(char)
            visited.add(char)
        return "".join(stack)
        