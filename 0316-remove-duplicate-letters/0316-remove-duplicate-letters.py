class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        boundries, stack, exist = {}, [], set()
        for i, char in enumerate(s):
            boundries[char] = i
        for i, char in enumerate(s):
            if char in exist: continue
            while stack and char < stack[-1] and i < boundries[stack[-1]]:
                node = stack.pop()
                exist.remove(node)
            stack.append(char)
            exist.add(char)
        return "".join(stack)
        
        