class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {"+": (lambda x, y: x + y), "-": (lambda x, y: x - y), "/": (lambda x, y: int(float(x) / y)), "*": (lambda x, y: x * y)}
        for t in tokens:
            if t in op:
                s1, s2 = stack.pop(), stack.pop()
                stack.append(op[t](s2, s1))
                # print(s1, t, s2)
            else:
                stack.append(int(t))
            # print(stack)
        return stack[0]