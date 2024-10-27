class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        total = 0

        for r in range(1, m+1):
            for c in range(1, n+1):
                if matrix[r-1][c-1] == 1:
                    dp[r][c] = min(dp[r][c-1], dp[r-1][c], dp[r-1][c-1]) + 1
                    total += dp[r][c]

        return total