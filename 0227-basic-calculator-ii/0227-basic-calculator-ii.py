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

        stack, cur_oper, cur_num = [], "+", 0
        for i in range(len(s)):
            if s[i].isdigit():
                cur_num = cur_num * 10 + int(s[i])
            elif s[i] in "+-*/":
                update()
                cur_oper, cur_num = s[i], 0
        update()
        return sum(stack)
        