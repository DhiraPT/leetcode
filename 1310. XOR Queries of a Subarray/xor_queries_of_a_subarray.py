class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        for i in arr:
            prefix_xor.append(prefix_xor[-1] ^ i)

        return [prefix_xor[r+1] ^ prefix_xor[l] for l, r in queries]