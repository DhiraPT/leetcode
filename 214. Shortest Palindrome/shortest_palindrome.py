class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def compute_lps(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length-1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        if not s or len(s) == 1:
            return s

        lps = compute_lps(s + '#' + s[::-1])
        longest_palindrome_prefix_len = lps[-1]
        return s[longest_palindrome_prefix_len:][::-1] + s