class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        i = 1
        for _ in range(n):
            res.append(i)
            if i * 10 <= n:
                i *= 10
            else:
                while i % 10 == 9 or i >= n:
                    i //= 10
                i += 1
        return res