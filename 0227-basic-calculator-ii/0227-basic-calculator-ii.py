class Solution:
    def calculate(self, s: str) -> int:
        def update(curOper):
            if curOper == "+":
                stack.append(curNum)
            elif curOper == "-":
                stack.append(-curNum)
            elif curOper == "*":
                stack.append(stack.pop() * curNum)
            else:
                stack.append(int(stack.pop() / curNum))
            

        i, curOper, stack = 0, "+", []
        while i < len(s):
            if s[i] in "+-*/":
                update(curOper)
                curOper = s[i]
            elif s[i].isdigit():
                curNum = 0
                while i < len(s) and s[i].isdigit():
                    curNum = curNum * 10 + int(s[i])
                    i += 1
                i -= 1
            i += 1
        update(curOper)
        return sum(stack)


            
        