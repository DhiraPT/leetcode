class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degrees = [0] * n
        for u, v in edges:
            in_degrees[v] += 1

        champion = -1
        for i in range(len(in_degrees)):
            if in_degrees[i] == 0:
                if champion == -1:
                    champion = i
                else:
                    return -1

        return champion