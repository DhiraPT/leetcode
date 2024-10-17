class Solution:
    def maximumSwap(self, num: int) -> int:
        if 0 <= num <= 9:
            return num

        num = list(str(num))
        n = len(num)

        max_i = n - 1
        x, y = -1, -1

        for i in range(n - 2, -1, -1):
            if num[i] > num[max_i]:
                max_i = i
            elif num[i] < num[max_i]:
                x, y = i, max_i

        if x != -1:
            num[x], num[y] = num[y], num[x]

        return int(''.join(num))