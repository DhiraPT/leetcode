class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0
    
    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.score += 1

    def get_total_score(self, word):
        curr = self
        total_score = 0
        for c in word:
            curr = curr.children[c]
            total_score += curr.score
        return total_score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        for w in words:
            root.insert(w)
        return [root.get_total_score(w) for w in words]