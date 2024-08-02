class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack, exists, positions = [], set(), {char: i for i, char in enumerate(s)}
        for i, char in enumerate(s):
            if char in exists: continue
            while stack and stack[-1] > char and i < positions[stack[-1]]:
                exists.remove(stack.pop())
            stack.append(char)
            exists.add(char)
        return "".join(stack)