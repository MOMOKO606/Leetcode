class Solution:
    def calculate(self, s: str) -> int:
        def get_num(j):
            num = 0
            while j < len(s) and s[j].isdigit():
                num = num * 10 + int(s[j])
                j += 1
            return num, j - 1 

        def update():
            if cur_oper == "+":
                stack.append(cur_num)
            elif cur_oper == "-":
                stack.append(-cur_num)
            elif cur_oper == "*":
                stack.append(stack.pop() * cur_num)
            else:
                stack.append(int(stack.pop() / cur_num))
        
        stack, cur_oper, j = [], "+", 0
        while j < len(s):
            if s[j] in "+-*/":
                update()
                cur_oper = s[j]
            elif s[j].isdigit():
                cur_num, j = get_num(j)
            elif s[j] == "(":
                cur_num, delta = self.calculate(s[j + 1:])
                j += delta
            elif s[j] == ")":
                update()
                return sum(stack), j + 1
            j += 1
        update()
        return sum(stack)
        

        