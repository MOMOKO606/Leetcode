class Solution:
    def isValid(self, s: str) -> bool:
        validator, stack = {")": "(", "]": "[", "}": "{"}, []
        for char in s:
            if char in "([{":
                stack.append(char)
            elif not stack or validator[char] != stack.pop(): return False
        return not stack