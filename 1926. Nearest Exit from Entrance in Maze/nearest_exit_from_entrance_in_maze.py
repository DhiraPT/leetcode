class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = {(entrance[0], entrance[1])}
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            r, c, steps = queue.popleft()
            if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and [r, c] != entrance:
                return steps
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < m and 0 <= new_c < n and maze[new_r][new_c] == '.' and (new_r, new_c) not in visited:
                    queue.append((new_r, new_c, steps + 1))
                    visited.add((new_r, new_c))

        return -1