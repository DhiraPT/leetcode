class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = deque()
        vowels_set = set('aeiouAEIOU')

        for i in range(len(s)-1, -1, -1):
            if s[i] in vowels_set:
                vowels.append(s[i])

        for i in range(len(s)):
            if s[i] in vowels_set:
                s_list[i] = vowels.popleft()

        return ''.join(s_list)