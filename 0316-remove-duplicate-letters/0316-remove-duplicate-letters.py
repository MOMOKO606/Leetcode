class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack, exists, boundries = [], set(), {char: i for i, char in enumerate(s)}
        for i, char in enumerate(s):
            if char in exists: continue
            while stack and stack[-1] > char and i < boundries[stack[-1]]:
                exists.remove(stack.pop())
            stack.append(char)
            exists.add(char)
        return "".join(stack)