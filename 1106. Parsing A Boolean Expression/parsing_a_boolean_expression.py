class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if len(expression) == 1:
            return expression == 't'

        stack = []
        for c in expression[::-1]:
            if c == ')' or c == 'f' or c == 't':
                stack.append(c)
            elif c == '!':
                res = 't' if stack.pop() == 'f' else 'f'
                stack.pop()
                stack.append(res)
            elif c == '|':
                res = False
                while stack and stack[-1] != ')':
                    res |= (stack.pop() == 't')
                stack.pop()
                stack.append('t' if res else 'f')
            elif c == '&':
                res = True
                while stack and stack[-1] != ')':
                    res &= (stack.pop() == 't')
                stack.pop()
                stack.append('t' if res else 'f')

        return stack.pop() == 't'