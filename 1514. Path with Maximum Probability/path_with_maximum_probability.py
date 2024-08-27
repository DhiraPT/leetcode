class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        AL = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            AL[u].append((v, succProb[i]))
            AL[v].append((u, succProb[i]))

        probs = [0 for _ in range(n)]
        probs[start_node] = 1
        pq = []
        heappush(pq, (-1, start_node))

        while pq:
            p, u = heappop(pq)
            p = -p
            if p < probs[u]:
                continue
            for v, w in AL[u]:
                new_p = probs[u] * w
                if new_p <= probs[v]:
                    continue
                probs[v] = new_p
                heappush(pq, (-probs[v], v))

        return probs[end_node]