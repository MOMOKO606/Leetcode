class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i, digit in enumerate(num):
            digit = int(digit)
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        while stack and k:
            stack.pop()
            k -= 1
        while stack and not stack[0]:
            stack.pop(0)
        return "".join(map(str, stack)) if stack else "0"