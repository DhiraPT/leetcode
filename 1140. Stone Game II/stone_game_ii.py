class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n-2, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]

        dp = [[0] * (n+1) for _ in range(n)]

        for i in range(n-1, -1, -1):
            for M in range(1, n+1):
                max_stones = 0
                for X in range(1, 2*M+1):
                    if i + X >= n:
                        max_stones = suffix_sum[i]
                    else:
                        max_stones = max(max_stones, suffix_sum[i] - dp[i + X][max(M, X)])
                dp[i][M] = max_stones

        return dp[0][1]