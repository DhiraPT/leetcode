class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        islands = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    islands += 1
                    queue = deque([(r, c)])
                    while queue:
                        r1, c1 = queue.popleft()
                        if 0 <= r1 < m and 0 <= c1 < n and grid[r1][c1] == '1':
                            grid[r1][c1] = '0'
                            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                                r2, c2 = r1 + dr, c1 + dc
                                if 0 <= r2 < m and 0 <= c2 < n and grid[r2][c2] == '1':
                                    queue.append((r2, c2))

        return islands