class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        count = 0

        for i in range(n):
            zeroes = 0
            ones = 0
            for j in range(i, n):
                if s[j] == '0':
                    zeroes += 1
                elif s[j] == '1':
                    ones += 1

                if zeroes <= k or ones <= k:
                    count += 1
                else:
                    break
        
        return count