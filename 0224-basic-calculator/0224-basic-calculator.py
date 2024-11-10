class Solution:
    def calculate(self, s: str) -> int:
        def update(curOper, curNum):
            if curOper == "+":
                stack.append(curNum)
            elif curOper == "-":
                stack.append(-curNum)


        stack, curOper, curNum, i = [], "+", 0, 0
        while i < len(s):
            if s[i].isdigit():
                curNum = curNum * 10 + int(s[i])
            elif s[i] in "+-":
                update(curOper, curNum)
                curOper, curNum = s[i], 0
            elif s[i] == "(":
                curNum, l = self.calculate(s[i + 1:])
                i += l
            elif s[i] == ")":
                update(curOper, curNum)
                return sum(stack), i + 1
            i += 1
        update(curOper, curNum)
        return sum(stack)

        