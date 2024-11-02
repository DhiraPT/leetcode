class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(' ')
        for i, word in enumerate(sentence):
            if word[0] != sentence[i-1][-1]:
                return False
        return True