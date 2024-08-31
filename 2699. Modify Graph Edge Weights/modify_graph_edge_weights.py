class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        def dijkstra(s, adj):
            dist = [2*10**9] * n
            dist[s] = 0
            pq = []
            heappush(pq, (0, s))
            while pq:
                d, u = heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in adj[u]:
                    if dist[u] + w >= dist[v]:
                        continue
                    dist[v] = dist[u] + w
                    heappush(pq, (dist[v], v))
            return dist

        adj = [[] for _ in range(n)]
        for i, (u, v, w) in enumerate(edges):
            if w == -1:
                continue
            adj[u].append((v, w))
            adj[v].append((u, w))

        d = dijkstra(source, adj)

        if d[destination] < target:
            return []

        if d[destination] == target:
            for i, (u, v, w) in enumerate(edges):
                if w == -1:
                    edges[i][2] = 2*10**9
            return edges

        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue
            edges[i][2] = 1
            adj[u].append((v, 1))
            adj[v].append((u, 1))
            d = dijkstra(source, adj)

            if d[destination] <= target:
                edges[i][2] += target - d[destination]
                for j in range(i+1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = 2*10**9
                return edges

        return []