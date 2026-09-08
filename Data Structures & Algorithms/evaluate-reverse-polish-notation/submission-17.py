class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        while(tokens):
            if tokens[0] not in ["*","-","/","+"]:
                num_stack.append(tokens[0])
            else:
                b = int(num_stack.pop())
                a = int(num_stack.pop())
                if tokens[0] == "+":
                    num_stack.append(a + b)
                elif tokens[0] == "-":
                    num_stack.append(a - b)
                elif tokens[0] == "*":
                    num_stack.append(a * b)
                elif tokens[0] == "/":
                    num_stack.append(int(a / b))
            tokens.pop(0)
        return int(num_stack.pop())
