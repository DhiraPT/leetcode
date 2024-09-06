class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            adj[a][b] = v
            adj[b][a] = 1/v

        def dfs(c, d, visited):
            if c not in adj or d not in adj:
                return -1.0

            if d in adj[c]:
                return adj[c][d]

            visited.add(c)

            for denom, val in adj[c].items():
                if denom not in visited:
                    product = dfs(denom, d, visited)
                    if product != -1.0:
                        return val * product

            return -1.0

        res = []
        for c, d in queries:
            if c == d and c in adj:
                res.append(1.0)
            else:
                res.append(dfs(c, d, set()))

        return res