class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod_counts = [0] * k
        for i in arr:
            mod_counts[i % k] += 1

        if mod_counts[0] % 2 != 0:
            return False

        for i in range(1, k//2+1):
            if i == k - i:
                if mod_counts[k//2] % 2 != 0:
                    return False
            elif mod_counts[i] != mod_counts[k-i]:
                return False

        return True