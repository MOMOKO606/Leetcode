class Solution:
    def calculate(self, s: str) -> int:
        def update():
            if cur_oper == "+":
                stack.append(cur_num)
            elif cur_oper == "-":
                stack.append(-cur_num)
            elif cur_oper == "*":
                stack.append(stack.pop() * cur_num)
            else:
                stack.append(int(stack.pop() / cur_num))

        cur_oper, cur_num, stack, i = "+", 0, [], 0
        while i < len(s):
            if s[i].isdigit():
                cur_num = cur_num * 10 + int(s[i])
            elif s[i] in "+-*/":
                update()
                cur_oper, cur_num = s[i], 0
            elif s[i] == "(":
                cur_num, j = self.calculate(s[i + 1:])
                i += j
            elif s[i] == ")":
                update()
                return sum(stack), i + 1
            i += 1
        update()
        return sum(stack)

        