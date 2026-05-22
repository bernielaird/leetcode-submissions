class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openClosed = {")" : "(", "]":"[", "}":"{"}
        for i in s:
            if i in openClosed:
                if stack and stack[-1] == openClosed[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        return False