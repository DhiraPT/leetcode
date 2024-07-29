class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)
        matrix = [[0] * cols for _ in range(rows)]

        r, c = 0, 0
        while r < rows and c < cols:
            val = min(rowSum[r], colSum[c])
            matrix[r][c] = val
            rowSum[r] -= val
            colSum[c] -= val
            if rowSum[r] == 0:
                r += 1
            elif colSum[c] == 0:
                c += 1

        return matrix
