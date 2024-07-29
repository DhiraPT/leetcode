class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def dijkstra(s, adj):
            dist = [math.inf] * n
            dist[s] = 0
            pq = []
            heappush(pq, (0, s))
            while (len(pq) > 0):
                d, u = heappop(pq)
                if (d > dist[u]):
                    continue
                for v, w in adj[u]:
                    if (dist[u] + w >= dist[v]):
                        continue
                    dist[v] = dist[u] + w
                    heappush(pq, (dist[v], v))
            return dist

        adj = [[] for u in range(n)]
        for e in edges:
            adj[e[0]].append((e[1], e[2]))
            adj[e[1]].append((e[0], e[2]))

        min_count = n
        city = -1
        for u in range(n):
            count = 0
            dist = dijkstra(u, adj)
            for d in dist:
                if d <= distanceThreshold:
                    count += 1
            if (count < min_count or (count == min_count and u > city)):
                min_count = count
                city = u

        return city
