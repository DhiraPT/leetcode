class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        fresh_count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        while queue:
            r, c, t = queue.popleft()
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 2
                    queue.append((new_r, new_c, t + 1))
                    fresh_count -= 1
                    if fresh_count == 0:
                        return t + 1

        return -1