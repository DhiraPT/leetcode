class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        substrings = set()

        def backtrack(s, start, substrings):
            if start == len(s):
                return 0

            max_count = 0
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub not in substrings:
                    substrings.add(sub)
                    max_count = max(max_count, 1 + backtrack(s, end, substrings))
                    substrings.remove(sub)

            return max_count

        return backtrack(s, 0, substrings)