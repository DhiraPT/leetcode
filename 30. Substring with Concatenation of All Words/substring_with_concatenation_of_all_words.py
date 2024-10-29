class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        substring_length = word_length * len(words)

        if substring_length > len(s):
            return []

        f = Counter(words)
        res = []

        for i in range(word_length):
            left = i
            right = i
            curr_f = Counter()

            while right + word_length <= len(s):
                word = s[right:right+word_length]
                right += word_length

                if word not in words:
                    left = right
                    curr_f.clear()
                else:
                    curr_f[word] = curr_f.get(word, 0) + 1
                    while curr_f[word] > f[word]:
                        curr_f[s[left:left+word_length]] -= 1
                        left += word_length
                    if right - left == substring_length:
                        res.append(left)

        return res