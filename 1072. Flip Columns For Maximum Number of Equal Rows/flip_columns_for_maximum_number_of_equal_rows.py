class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        row_counts = {}

        for row in matrix:
            tuple_row = tuple(row)
            complement = tuple(1 - x for x in row)
            row_counts[tuple_row] = row_counts.get(tuple_row, 0) + 1
            row_counts[complement] = row_counts.get(complement, 0) + 1

        return max(row_counts.values())