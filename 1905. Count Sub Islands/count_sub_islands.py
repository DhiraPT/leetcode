class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid2[r][c] == 0:
                return True

            grid2[r][c] = 0

            is_sub = grid1[r][c] == 1
            is_sub &= dfs(r, c+1)
            is_sub &= dfs(r, c-1)
            is_sub &= dfs(r+1, c)
            is_sub &= dfs(r-1, c)

            return is_sub

        count = 0
        for r in range(m):
            for c in range(n):
                if grid2[r][c] == 1 and dfs(r, c):
                    count += 1

        return count