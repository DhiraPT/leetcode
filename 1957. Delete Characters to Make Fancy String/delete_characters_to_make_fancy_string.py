class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[:2].split()

        for i in range(2, len(s)):
            if s[i] == s[i-1] and s[i] == s[i-2]:
                continue
            res.append(s[i])

        return ''.join(res)