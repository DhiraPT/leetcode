class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        matrix = []
        for i in range(0, len(original), n):
            matrix.append(original[i:i+n])

        return matrix