class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i, char in enumerate(num):
            while k and stack and int(char) < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(int(char))
        
        while k and stack:
            stack.pop()
            k -= 1

        while stack and not stack[0]:
            stack.pop(0)

        return "".join(map(str, stack)) if stack else "0"

        