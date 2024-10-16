class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        f = {'a': 0, 'b': 0, 'c': 0}
        s = ''

        while f['a'] < a or f['b'] < b or f['c'] < c:
            chars = sorted(['a', 'b', 'c'], key=lambda x: (a - f['a']) if x == 'a' else (b - f['b']) if x == 'b' else (c - f['c']), reverse=True)
            added = False
            for i in chars:
                if len(s) >= 2 and s[-2] == s[-1] and i == s[-1]:
                    continue
                if i == 'a' and f[i] == a:
                    continue
                if i == 'b' and f[i] == b:
                    continue
                if i == 'c' and f[i] == c:
                    continue
                s += i
                f[i] += 1
                added = True
                break

            if not added:
                break

        return s