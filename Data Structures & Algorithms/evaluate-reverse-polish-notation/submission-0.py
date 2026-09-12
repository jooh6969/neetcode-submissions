class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                first = stack.pop()
                second = stack.pop()
                operation = tokens[i]
                if operation == '+':
                    stack.append(second + first)
                elif operation == '-':
                    stack.append(second - first)
                elif operation == '*':
                    stack.append(second * first)
                else:
                    stack.append(int(second / first))
        return stack.pop()
                