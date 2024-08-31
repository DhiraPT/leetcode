class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = ''

        for i in range(0, len(s), k):
            substring = s[i:i+k]
            total = sum(ord(c) - ord('a') for c in substring)
            res += chr(ord('a') + total % 26)
        
        return res