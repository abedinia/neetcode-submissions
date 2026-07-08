class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        shapes = {
            "]":"[",
            ")":"(",
            "}":"{",
        }

        stack = []

        for char in s:
            if char in shapes.values():
                stack.append(char)
            elif char in shapes.keys():
                if len(stack) == 0:
                    return False

                if stack[-1] == shapes[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        if len(stack) == 0:
            return True
        return False