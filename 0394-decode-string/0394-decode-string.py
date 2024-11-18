class Solution:
    def decodeString(self, s: str) -> str:
        stack, curNum, ans = [], 0, ""
        for char in s:
            if char.isdigit():
                curNum = curNum * 10 + int(char)
            elif char == "[":
                stack.append(curNum)
                curNum = 0
            elif char == "]":
                curStr = []
                while isinstance(stack[-1], str):
                    curStr.append(stack.pop())
                stack.append("".join(curStr[::-1]) * stack.pop())
            else:
                stack.append(char)
        
        return "".join(stack)

        