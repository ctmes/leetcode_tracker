from math import ceil, floor

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                b, a = stack.pop(), stack.pop()

                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                else:
                    division = a / b
                    if division < 0:
                        stack.append(ceil(division))
                    else:
                        stack.append(floor(division))

            else:
                stack.append(int(token))
        
        return stack[0]

