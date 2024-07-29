class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = [('(', 1 , 0)]

        while stack:
            s, o, c = stack.pop()
            if len(s) == 2 * n:
                res.append(s)
                continue
            if o < n:
                stack.append((s + '(', o + 1, c))
            if c < o:
                stack.append((s + ')', o, c + 1))
        
        return res
