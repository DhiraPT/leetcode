class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        n_sum = mean * (n + len(rolls)) - sum(rolls)

        if n_sum < n or n_sum > 6 * n:
            return []

        val, remainder = divmod(n_sum, n)

        return [val + 1] * remainder + [val] * (n - remainder)