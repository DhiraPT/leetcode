class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split(' ')
        sentence2 = sentence2.split(' ')
        n = min(len(sentence1), len(sentence2))
        lcp = lcs = 0

        for i in range(n):
            if sentence1[i] == sentence2[i]:
                lcp += 1
            else:
                break

        for i in range(n):
            if sentence1[-i-1] == sentence2[-i-1]:
                lcs += 1
            else:
                break

        return lcp + lcs >= n