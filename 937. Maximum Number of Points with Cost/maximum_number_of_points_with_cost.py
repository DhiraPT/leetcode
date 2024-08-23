class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0]

        for r in range(1, m):
            for c in range(1, n):
                dp[c] = max(dp[c], dp[c-1] - 1)

            for c in range(n - 2, -1, -1):
                dp[c] = max(dp[c], dp[c+1] - 1)

            for c in range(n):
                dp[c] += points[r][c]

        return max(dp)