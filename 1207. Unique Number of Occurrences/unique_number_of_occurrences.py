class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = Counter(arr).values()
        return len(set(occ)) == len(occ)