class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        min_heap = [(0, 0, 0)]
        dist[0][0] = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while min_heap:
            curr_dist, r, c = heapq.heappop(min_heap)
            if curr_dist > dist[r][c]:
                continue
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < m and 0 <= new_c < n:
                    new_dist = dist[r][c] + grid[new_r][new_c]
                    if new_dist < dist[new_r][new_c]:
                        dist[new_r][new_c] = new_dist
                        heapq.heappush(min_heap, (new_dist, new_r, new_c))

        return dist[m-1][n-1]