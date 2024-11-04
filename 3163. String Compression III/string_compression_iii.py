class Solution:
    def compressedString(self, word: str) -> str:
        comp_list = []

        start = 0
        for i, c in enumerate(word):
            if c != word[start] or i - start >= 9:
                comp_list.append(f'{i - start}{word[start]}')
                start = i
        comp_list.append(f'{len(word) - start}{word[start]}')

        return ''.join(comp_list)