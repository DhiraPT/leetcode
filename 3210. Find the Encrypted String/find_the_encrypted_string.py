class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        res = ''
        n = len(s)
        for i in range(n):
            res += s[(i + k) % n]
        return res