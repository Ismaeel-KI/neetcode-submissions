class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        i = 0
        sym = "+-*/"
        val = 0

        while i < n:
            if tokens[i] in sym:
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == '+':
                    stack.append(a + b)
                elif tokens[i] == '-':
                    stack.append(a - b)
                elif tokens[i] == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
    
            else:
                stack.append(int(tokens[i]))
            
            i += 1

        return stack[-1]