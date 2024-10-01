class Solution:
    def calculate(self, s: str) -> int:
        def helper(curOper, curNum):
            if curOper == "+":
                stack.append(curNum)
            elif curOper == "-":
                stack.append(-curNum)
            elif curOper == "*":
                stack.append(stack.pop() * curNum)
            elif curOper == "/":
                stack.append(int(stack.pop() / curNum))

        stack, curOper, curNum = [], "+", 0
        for char in s:
            if char.isdigit():
                curNum = curNum * 10 + int(char)
            elif char in "+-*/":
                helper(curOper, curNum)
                curOper, curNum = char, 0
        helper(curOper, curNum)
        return sum(stack)

        