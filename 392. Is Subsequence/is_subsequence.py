class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        if len(s) > len(t):
            return False

        i = 0
        for c in t:
            if s[i] == c:
                i += 1
            if i >= len(s):
                return True

        return False