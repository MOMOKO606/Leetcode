class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+": stack.append(num1 + num2) 
                elif token == "-": stack.append(num1 - num2)
                elif token == "*": stack.append(num1 * num2) 
                elif token == "/": stack.append(int(num1 / num2))
            else: stack.append(int(token))
        return stack.pop()
        