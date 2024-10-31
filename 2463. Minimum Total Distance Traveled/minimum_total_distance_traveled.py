class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        m, n = len(robot), len(factory)
        robot.sort()
        factory.sort(key=lambda x: x[0])

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        for i in range(n + 1):
            dp[0][i] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j-1]
                total_distance = 0
                for k in range(1, min(factory[j-1][1], i) + 1):
                    total_distance += abs(robot[i-k] - factory[j-1][0])
                    dp[i][j] = min(dp[i][j], dp[i-k][j-1] + total_distance)

        return dp[m][n]