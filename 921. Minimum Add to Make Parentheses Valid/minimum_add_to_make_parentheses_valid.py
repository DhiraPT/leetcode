class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = close = 0
        for c in s:
            if c == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    close += 1
        return open + close