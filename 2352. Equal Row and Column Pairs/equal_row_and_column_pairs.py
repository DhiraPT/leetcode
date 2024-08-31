class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_f = Counter(tuple(row) for row in grid)
        column_f = Counter(tuple(row[c] for row in grid) for c in range(len(grid[0])))

        count = 0
        for row, f in row_f.items():
            if row in column_f:
                count += f * column_f[row]

        return count