class Solution:
    def minimumSteps(self, s: str) -> int:
        count_1 = 0
        steps = 0

        for c in s:
            if c == '1':
                count_1 += 1
            else:
                steps += count_1

        return steps