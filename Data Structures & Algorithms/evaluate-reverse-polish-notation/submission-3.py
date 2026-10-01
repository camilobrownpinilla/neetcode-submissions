class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'*': lambda x, y: x * y, 
                    '/': lambda x, y : x / y,
                    '-': lambda x , y: x - y, 
                    '+': lambda x, y: x + y}
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                int1 = stack.pop()
                int2 = stack.pop()
                stack.append(operators[t](int(int2), int(int1)))

        return int(stack[0])