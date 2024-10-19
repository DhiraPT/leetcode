class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'

        num_bits = (1 << n) - 1

        if k == (num_bits // 2) + 1:
            return '1'

        if k < (num_bits // 2) + 1:
            return self.findKthBit(n - 1, k)

        return '0' if self.findKthBit(n - 1, num_bits - k + 1) == '1' else '1'