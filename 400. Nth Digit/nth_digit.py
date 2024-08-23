class Solution:
    def findNthDigit(self, n: int) -> int:
        m = 1
        total_digits = 9

        while n > total_digits:
            n -= total_digits
            m += 1
            total_digits = (10**m - 10**(m-1)) * m

        num = 10**(m-1) + (n - 1) // m
        return int(str(num)[(n-1) % m])