class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        def djikstra(s, adj):
            dist = [math.inf] * 26
            dist[ord(s) - ord('a')] = 0
            pq = []
            heappush(pq, (0, ord(s) - ord('a')))
            while (len(pq) > 0):
                d, u = heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in adj[u]:
                    if dist[u] + w >= dist[v]:
                        continue
                    dist[v] = dist[u] + w
                    heappush(pq, (dist[v], v))
            return dist

        adj = [[] for _ in range(26)]
        for i in range(len(changed)):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            adj[u].append((v, cost[i]))
        
        total_cost = 0
        dist_map = {}
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            if source[i] in dist_map:
                dist = dist_map[source[i]]
            else:
                dist = djikstra(source[i], adj)
                dist_map[source[i]] = dist
            cost = dist[ord(target[i]) - ord('a')]
            if math.isinf(cost):
                return -1
            total_cost += cost

        return total_cost
