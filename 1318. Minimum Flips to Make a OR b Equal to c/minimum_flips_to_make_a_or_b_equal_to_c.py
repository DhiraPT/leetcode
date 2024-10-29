class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flip = 0

        while a or b or c:
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1

            if c_bit == 0:
                flip += a_bit + b_bit
            else:
                if a_bit == 0 and b_bit == 0:
                    flip += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return flip