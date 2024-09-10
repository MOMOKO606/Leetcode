class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack, visited, boundaries = [], set(), {char: i for i, char in enumerate(s)}
        for i, char in enumerate(s):
            if char in visited: continue
            while stack and char < stack[-1] and boundaries[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(char)
            visited.add(char)
        return "".join(stack)
        
        