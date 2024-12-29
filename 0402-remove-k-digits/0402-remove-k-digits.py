class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for j, char in enumerate(num):
            while stack and k and stack[-1] > int(char):
                stack.pop()
                k -= 1
            stack.append(int(char))

        while stack and k:
            stack.pop()
            k -= 1

        while stack and not stack[0]:
            stack.pop(0)
        return "".join(map(str, stack)) if stack else "0"
            
        