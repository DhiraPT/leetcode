class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        max_sum = 0
        negative_count = 0
        largest_negative = -float('inf')

        for row in matrix:
            for e in row:
                if e < 0:
                    max_sum -= e
                    negative_count += 1
                    largest_negative = max(largest_negative, e)
                else:
                    max_sum += e
                    largest_negative = max(largest_negative, -e)

        return max_sum if negative_count % 2 == 0 else max_sum + 2 * largest_negative