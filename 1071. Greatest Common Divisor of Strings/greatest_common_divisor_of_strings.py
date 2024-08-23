class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divisor = ''

        if str1 + str2 != str2 + str1:
            return divisor

        gcd = 1
        for i in range(min(len(str1), len(str2)), 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                gcd = i
                break

        for i in range(gcd):
            if str1[i] != str2[i]:
                break
            divisor += str1[i]

        return divisor