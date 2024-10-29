class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        curr = [0] * m

        for c in range(n-2, -1, -1):
            prev = [0] * m
            for r in range(m):
                for r2 in range(r-1, r+2):
                    if 0 <= r2 < m and grid[r][c] < grid[r2][c+1]:
                        prev[r] = max(prev[r], curr[r2] + 1)
            curr = prev[:]

        return max(curr)