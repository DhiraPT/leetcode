class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        a, b, c = 1, 2, 5
        for i in range(4, n+1):
            a, b, c = b, c, (c * 2 + a) % (10**9 + 7)

        return c