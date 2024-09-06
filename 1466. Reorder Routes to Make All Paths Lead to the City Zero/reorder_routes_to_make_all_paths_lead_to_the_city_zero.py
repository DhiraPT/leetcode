class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()

        def dfs(city, count):
            for c, d in adj[city]:
                if c not in visited:
                    visited.add(c)
                    if d == 1:
                        count += 1
                    count = dfs(c, count)
            return count

        adj = [[] for _ in range(n)]
        for c1, c2 in connections:
            adj[c1].append((c2, 1))
            adj[c2].append((c1, 0))

        visited.add(0)
        return dfs(0, 0)