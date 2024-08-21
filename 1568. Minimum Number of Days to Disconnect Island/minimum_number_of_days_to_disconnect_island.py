class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.numdisjoint = n

    def find(self, x):
        xp = x
        children = []
        while xp != self.parents[xp]:
            children.append(xp)
            xp = self.parents[xp]
        for c in children:
            self.parents[c] = xp
        return xp

    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return

        if self.ranks[ap] < self.ranks[bp]:
            self.parents[ap] = bp
            self.sizes[bp] += self.sizes[ap]
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
            self.sizes[ap] += self.sizes[bp]
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1
            self.sizes[ap] += self.sizes[bp]

        self.numdisjoint -= 1

    def size(self, x):
        return self.sizes[self.find(x)]

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def is_connected():
            ufds = UFDS(m * n)
            directions = [(0, 1), (1, 0)]

            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1:
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                                ufds.union(r * n + c, nr * n + nc)

            root = None
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1:
                        if root is None:
                            root = ufds.find(r * n + c)
                        elif root != ufds.find(r * n + c):
                            return False
            return root is not None

        if not is_connected():
            return 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    if not is_connected():
                        return 1
                    grid[r][c] = 1

        return 2