class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for l in logs:
            if l != "./":
                if l != "../":
                    stack.append(l)
                else:
                    if len(stack) != 0:
                        stack.pop()
        
        return len(stack)