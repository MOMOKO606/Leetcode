class Solution:
    def isValid(self, s: str) -> bool:
        stack, match, s = [], {"(": ")", "[": "]", "{": "}"}, list(s)
        while s:
            sign = s.pop()
            if sign in [")", "]", "}"]: stack.append(sign)
            elif not stack or match[sign] != stack.pop(): return False
        return not stack 
        