class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(["+","-","*","/"])
        for i in tokens:
            if i not in ops:
                stack.append(i)
            else:
                print(stack)
                x = stack.pop()
                y = stack.pop()
                stack.append(str(int(eval((y + i + x)))))
        return int(stack.pop())
                

