class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        def dijkstra(s: int, adj: List[List[int]]) -> List[int]:
            time1 = [math.inf] * (n + 1)
            time2 = [math.inf] * (n + 1)
            time1[s] = 0
            pq = []
            heappush(pq, (0, s))

            while pq:
                t, u = heappop(pq)
                if t > time2[u]:
                    continue

                for v in adj[u]:
                    t_arrival = t
                    if (t_arrival // change) % 2 == 1:
                        t_arrival = (t_arrival // change + 1) * change
                    t_arrival += time

                    if t_arrival < time1[v]:
                        time1[v], t_arrival = t_arrival, time1[v]
                        heappush(pq, (time1[v], v))
                    if time1[v] < t_arrival < time2[v]:
                        time2[v] = t_arrival
                        heappush(pq, (time2[v], v))

            return time2

        adj = [[] for _ in range(n + 1)]
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        time2 = dijkstra(1, adj)

        return time2[n]
