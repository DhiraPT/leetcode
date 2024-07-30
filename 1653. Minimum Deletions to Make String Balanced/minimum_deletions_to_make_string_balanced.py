class Solution:
    def minimumDeletions(self, s: str) -> int:
        min_remove = 0
        left_b_count = 0

        for c in s:
            if c == 'b':
                left_b_count += 1
            else:
                min_remove = min(min_remove + 1, left_b_count)

        return min_remove
