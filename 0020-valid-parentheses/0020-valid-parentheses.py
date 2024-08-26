class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
            }
        stack = []
        for char in s:
            if char in "([{": stack.append(char)
            elif not stack or pairs[stack.pop()] != char: return False
        return not stack
        



        