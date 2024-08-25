class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack, boundaries, exist = [], {char: i for i, char in enumerate(s)}, set()
        for i, char in enumerate(s):
            if char in exist: continue
            while stack and stack[-1] > char and i < boundaries[stack[-1]]:
                exist.remove(stack.pop())
            stack.append(char)
            exist.add(char)
        return "".join(stack)



        