class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def dfs(src, adj, visited, cur_path, res):
            if src in cur_path:
                return False
            if src in visited:
                return True
            visited.add(src)
            cur_path.add(src)
            for neighbor in adj[src]:
                if not dfs(neighbor, adj, visited, cur_path, res):
                    return False
            cur_path.remove(src)
            res.append(src)
            return True
    
        def topoSort(edges: List[int]):
            adj = defaultdict(list)
            for i in range(1, k+1):
                adj[i] = []
            for src, dst in edges:
                adj[src].append(dst)
            visited = set()
            cur_path = set()
            res = []
            for j in range(1, k+1):
                if not dfs(j, adj, visited, cur_path, res):
                    return []
            return res[::-1]

        sorted_row = topoSort(rowConditions)
        sorted_col = topoSort(colConditions)

        if not sorted_row or not sorted_col:
            return []
        
        pos = {i: [0, 0] for i in range(1, k+1)}
        for i, r in enumerate(sorted_row):
            pos[r][0] = i
        for i, c in enumerate(sorted_col):
            pos[c][1] = i

        res = [[0 for _ in range(k)] for _ in range(k)]
        for value in range(1, k+1):
            row, column = pos[value]
            res[row][column] = value

        return res
