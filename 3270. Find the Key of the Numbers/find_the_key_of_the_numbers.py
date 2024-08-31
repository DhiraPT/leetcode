class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        key = 0
        place = 1
        for _ in range(4):
            key += min(num1 % 10, num2 % 10, num3 % 10) * place
            num1 //= 10
            num2 //= 10
            num3 //= 10
            place *= 10
        return key