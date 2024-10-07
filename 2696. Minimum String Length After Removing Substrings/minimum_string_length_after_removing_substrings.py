class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if (stack[-1] == 'A' and c == 'B') or (stack[-1] == 'C' and c == 'D'):
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack)