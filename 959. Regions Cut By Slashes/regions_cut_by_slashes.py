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
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        ufds = UFDS(n * n * 4)

        for r in range(n):
            for c in range(n):
                index = 4 * (r * n + c)
                char = grid[r][c]

                if char == '/':
                    ufds.union(index, index + 3)
                    ufds.union(index + 1, index + 2)
                elif char == '\\':
                    ufds.union(index, index + 1)
                    ufds.union(index + 2, index + 3)
                elif char == ' ':
                    ufds.union(index, index + 1)
                    ufds.union(index, index + 2)
                    ufds.union(index, index + 3)

                if r < n - 1:
                    ufds.union(index + 2, index + 4 * n)
                if c < n - 1:
                    ufds.union(index + 1, index + 7)

        return ufds.numdisjoint