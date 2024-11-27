class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i + 1] if i < n - 1 else [] for i in range(n)]

        def bfs():
            dist = [float('inf')] * n
            dist[0] = 0
            queue = deque([0])

            while queue:
                city = queue.popleft()
                for v in adj[city]:
                    if dist[city] + 1 < dist[v]:
                        dist[v] = dist[city] + 1
                        queue.append(v)

            return dist[n-1]

        res = [n-1] * len(queries)
        for i, (u, v) in enumerate(queries):
            adj[u].append(v)
            res[i] = bfs()

        return res