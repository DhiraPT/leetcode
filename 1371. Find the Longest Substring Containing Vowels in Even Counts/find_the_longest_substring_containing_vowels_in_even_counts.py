class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_bit = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        curr_xor = 0
        xor_index = {0: -1}
        max_length = 0

        for i, c in enumerate(s):
            if c in vowel_bit:
                curr_xor ^= vowel_bit[c]
            if curr_xor in xor_index:
                max_length = max(max_length, i - xor_index[curr_xor])
            else:
                xor_index[curr_xor] = i

        return max_length