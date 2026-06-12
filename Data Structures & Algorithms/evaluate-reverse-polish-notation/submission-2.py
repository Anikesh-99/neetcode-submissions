class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: int(float(x) / y)}
        for i in range(len(tokens)):
            if tokens[i] in ops:
                a, b = stack.pop(), stack.pop()
                stack.append(ops[tokens[i]](b, a))
            else:
                stack.append(int(tokens[i]))
        return stack[0]
