class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digits_sum = 0
        for c in s:
            val = ord(c) - ord('a') + 1
            digits_sum += val // 10 + val % 10

        for _ in range(k-1):
            res = 0
            while digits_sum > 0:
                res += digits_sum % 10
                digits_sum //= 10
            digits_sum = res

        return digits_sum