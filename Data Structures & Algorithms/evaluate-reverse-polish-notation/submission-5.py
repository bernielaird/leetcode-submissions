class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(["+","-","*","/"])
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                x = stack.pop()
                y = stack.pop()
                if i == "+":
                    stack.append(x + y)
                if i == "-":
                    stack.append(y - x)
                if i == "*":
                    stack.append(x * y)
                if i == "/":
                    stack.append(int(y / x))
        return stack.pop()