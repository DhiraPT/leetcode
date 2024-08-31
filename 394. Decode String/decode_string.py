class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        string = ''
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                stack.append((string, k))
                string = ''
                k = 0
            elif c.isalpha():
                string += c
            else:
                prev_string, prev_k = stack.pop()
                string = prev_string + string * prev_k

        return string