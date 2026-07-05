class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if str(i) == "C":
                stack.pop()
            elif str(i) == "D":
                stack.append(int(stack[-1])*2)
            elif str(i) == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            else:
                stack.append(i)

        output = 0
        for i in stack:
            output += int(i)
        return output