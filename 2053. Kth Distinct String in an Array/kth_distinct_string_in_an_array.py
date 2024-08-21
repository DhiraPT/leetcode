class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        string_counts = Counter(arr)

        for string in arr:
            if string_counts[string] == 1:
                k -= 1
                if k == 0:
                    return string

        return ""