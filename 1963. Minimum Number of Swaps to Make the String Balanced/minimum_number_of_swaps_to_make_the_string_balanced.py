class Solution:
    def minSwaps(self, s: str) -> int:
        unbalanced = 0
        max_unbalanced = 0

        for c in s:
            if c == '[':
                unbalanced += 1
            elif c == ']':
                unbalanced -= 1

            max_unbalanced = min(max_unbalanced, unbalanced)

        return (-max_unbalanced + 1) // 2