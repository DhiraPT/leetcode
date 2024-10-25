class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, path):
        curr = self
        is_folder = True
        path_list = [f for f in path.split('/') if f]
        for f in path_list:
            if f in curr.children and curr.children[f].is_end:
                return False
            if f not in curr.children:
                curr.children[f] = TrieNode()
            curr = curr.children[f]
        curr.is_end = True
        return True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []

        root = TrieNode()
        for path in folder:
            if root.insert(path):
                res.append(path)

        return res